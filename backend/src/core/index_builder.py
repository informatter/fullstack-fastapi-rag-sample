import os
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from llama_index.core.schema import Document
from structlog.stdlib import BoundLogger
from typing import Optional, Sequence
from core.logging import get_logger
from core.config import build_settings ,LOCAL_ENV_NAME,TEST_ENV_NAME

RAG_STORAGE_DIR_NAME = "local_rag_storage"
logger: BoundLogger = get_logger()


def index_builder() -> VectorStoreIndex | None:
    settings = build_settings()
    if settings.env == LOCAL_ENV_NAME or settings.env  == TEST_ENV_NAME: 
        return __local_index_builder()
    else:
        raise Exception("index builder is not implemented for prod envs")


def __create_vector_store_index(
    documents: Sequence[Document] | None,
) -> VectorStoreIndex | None:
    """Creates a vector store index from a collection of documents
    For more info see: https://docs.llamaindex.ai/en/stable/understanding/indexing/indexing.html

    Returns:
    ------
    A  VectorStoreIndex or None of the operation failed.

    """
    try:
        return VectorStoreIndex.from_documents(documents)
    except Exception as e:
        logger.error("local_index_builder_error", error=e)

    return None


def __local_index_builder() -> VectorStoreIndex | None:
    """
    Creates a vector embeddings model from the documents, ready to be queried by an LLM.
    The embeddings will be cached to disk to avoid any extra to any 3rd party API's
    Returns:
    ------
    A  VectorStoreIndex or None of the operation failed.
    """
    # Get the current  directory
    current_script_directory = os.path.dirname(os.path.realpath(__file__))
    # Go one level up to the parent directory
    project_root = os.path.abspath(os.path.join(current_script_directory, os.pardir))

    rag_storage_dir_path = os.path.join(project_root, RAG_STORAGE_DIR_NAME)

    # Construct the path to the data folder
    data_folder_path = os.path.join(project_root, "local_rag_data")

    # documents = SimpleDirectoryReader(data_folder_path).load_data()
    index: VectorStoreIndex = None

    if not os.path.exists(rag_storage_dir_path):
        # load the documents and create the index
        documents = SimpleDirectoryReader(data_folder_path).load_data()

        index: VectorStoreIndex | None = __create_vector_store_index(documents)
        if index is None:
            return
        # store it for later
        index.storage_context.persist(persist_dir=rag_storage_dir_path)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=rag_storage_dir_path)
        index = load_index_from_storage(storage_context)
    return index
