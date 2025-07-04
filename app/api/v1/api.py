from fastapi import APIRouter

from app.api.v1.endpoints import echo

# Create the main API router for v1
api_router = APIRouter()

# Include the echo router
api_router.include_router(echo.router, prefix="/v1", tags=["echo"])
