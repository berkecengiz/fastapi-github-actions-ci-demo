import logging

from fastapi import APIRouter

from app.schemas.echo import EchoRequest, EchoResponse

# Configure logging
logger = logging.getLogger(__name__)

# Create a new router
router = APIRouter()


@router.post("/echo", response_model=EchoResponse, summary="Echo a message")
async def echo(request: EchoRequest):
    """
    Echoes the received message back to the client.
    This endpoint is now part of its own router.
    """
    logger.info(f"Received message to echo: {request.message}")
    return {"message": request.message}
