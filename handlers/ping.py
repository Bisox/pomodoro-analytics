from fastapi import APIRouter

from settings import Settings


router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/db")
async def get_db():
    settings = Settings()

    return {"db": settings.GOOGLE_TOKEN_ID}


@router.post("/app")
async def get_app():
    return {"app": "ok"}


