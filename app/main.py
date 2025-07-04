import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette import status

from app.core.config import Settings
from app.api.v1.api import api_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load application settings
settings = Settings()

# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="A demo FastAPI application with a CI/CD pipeline.",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler for a generic error
@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"An unexpected error occurred: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred.",
        },
    )

# API Endpoints
@app.get("/", summary="Health check endpoint")
async def health_check():
    """Simple health check endpoint to confirm the service is running."""
    return {"status": "ok"}

# Include the main API router
app.include_router(api_router)