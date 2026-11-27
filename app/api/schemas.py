
from pydantic import BaseModel, Field


class DebugRequest(BaseModel):
    code: str = Field(
        ...,
        min_length=1,
        description="Python code to debug"
    )


class DebugResponse(BaseModel):
    success: bool
    syntax_check: dict
    ai_analysis: str
