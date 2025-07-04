from pydantic import BaseModel, Field, field_validator

class EchoRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Message to be echoed")

    @field_validator("message")
    @classmethod
    def message_must_not_be_empty(cls, v: str) -> str:
        """Validate that the message is not empty or just whitespace."""
        if not v.strip():
            raise ValueError("Message cannot be empty or contain only whitespace")
        return v

class EchoResponse(BaseModel):
    message: str
