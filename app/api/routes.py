
from fastapi import APIRouter, HTTPException

from app.api.schemas import DebugRequest, DebugResponse
from app.services.debugger import debug_code

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "AI Code Debugger API is running!"
    }


@router.post("/debug", response_model=DebugResponse)
def debug(request: DebugRequest):
    try:
        result = debug_code(request.code)

        return {
            "success": True,
            "syntax_check": result["syntax_check"],
            "ai_analysis": result["ai_analysis"]
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )
