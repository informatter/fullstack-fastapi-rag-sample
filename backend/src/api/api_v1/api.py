from fastapi import APIRouter
from api.api_v1.endpoints import hellow


api_router = APIRouter()

api_router.include_router(hellow.router, prefix="/hellow_llama", tags=["hellow_llama"])