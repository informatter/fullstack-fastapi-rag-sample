from fastapi import APIRouter
from api.api_v1.routers import hellow
from api.api_v1.routers import query


api_router = APIRouter()

api_router.include_router(hellow.router, prefix="/hellow_llama", tags=["hellow_llama"])
api_router.include_router(query.router, prefix="/query", tags=["query"])
