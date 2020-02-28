from fastapi import APIRouter

from fastdash.api.routes import fastdash

router = APIRouter()
router.include_router(fastdash.router, tags=["fastdash"], prefix="/fastdash")
