from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/review", tags=["Review"])

class ReviewRequest(BaseModel):
    language: str
    source_code: str

@router.post("")
async def review_code(req: ReviewRequest):
    """
    Analyze the code using AI (like OpenAI or Hugging Face) 
    and return review comments.
    """
    code = req.source_code

    # Example placeholder logic (replace with actual AI call)
    review_comments = [
        "Code runs correctly.",
        "Consider adding comments for readability.",
        "Use list comprehensions for shorter loops in Python."
    ]

    return {"review": review_comments}
