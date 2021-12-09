from fastapi import APIRouter

from api.version1 import user_router, jobs_router


api_router = APIRouter()
api_router.include_router(user_router.router, prefix="/register", tags=["Users"])
api_router.include_router(jobs_router.router, prefix="/job", tags=["Job"])