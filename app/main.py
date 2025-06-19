import logging
import time
from contextlib import asynccontextmanager
from typing import Dict, Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from .config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.log_level.upper()),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


# Pydantic models
class HealthResponse(BaseModel):
    status: str
    timestamp: float
    version: str = settings.app_version


class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)


class MessageResponse(BaseModel):
    echo: str
    length: int
    timestamp: float


# Startup/shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up FastAPI application")
    yield
    logger.info("Shutting down FastAPI application")


# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    description="A robust FastAPI application with CI/CD pipeline",
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)

# Add security middleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=settings.allowed_hosts)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    # Log request
    logger.info(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    # Log response
    process_time = time.time() - start_time
    logger.info(f"Response: {response.status_code} - {process_time:.4f}s")

    return response


# Exception handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.error(f"HTTP {exc.status_code}: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500, content={"error": "Internal server error", "status_code": 500}
    )


# Routes
@app.get("/", response_model=Dict[str, str])
async def read_root():
    """Root endpoint returning basic status"""
    return {"status": "ok", "message": "FastAPI CI Demo is running!"}


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint for monitoring"""
    return HealthResponse(status="healthy", timestamp=time.time())


@app.post("/echo", response_model=MessageResponse)
async def echo_message(request: MessageRequest):
    """Echo endpoint that returns the message with metadata"""
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    return MessageResponse(
        echo=request.message, length=len(request.message), timestamp=time.time()
    )


@app.get("/version")
async def get_version():
    """Get application version"""
    return {"version": settings.app_version, "name": settings.app_name}


# Add a route that can simulate errors for testing
@app.get("/error")
async def simulate_error():
    """Endpoint to test error handling"""
    raise HTTPException(status_code=500, detail="This is a simulated error")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
