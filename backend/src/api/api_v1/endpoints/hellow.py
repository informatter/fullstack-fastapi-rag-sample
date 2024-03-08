from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=str | None)
def hellow_world():
    return "Hellow 🦙!"