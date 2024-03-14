from typing import Optional
from fastapi import APIRouter, HTTPException
from llama_index.core import VectorStoreIndex
from core.index_builder import index_builder
from llama_index.core.indices.base import BaseIndex

router = APIRouter()


@router.post("/", response_model=str | None)
def query_over_docs(user_query: str):
    vector_store_index = index_builder()
    if vector_store_index is None:
        raise HTTPException(
            status_code=409,
            detail="Your query could not be completed. Please try again",
        )

    query_engine = vector_store_index.as_query_engine()
    result = query_engine.query(user_query)

    return result.response  # pyright: ignore reportAttributeAccessIssue
