from fastapi import APIRouter

from app.llm.rag import ask_rag
from app.models.schemas import (
    QuestionRequest,
    AnswerResponse,
)

router = APIRouter()


@router.post(
    "/ask",
    response_model=AnswerResponse,
)
def ask_question(
    request: QuestionRequest,
):
    answer = ask_rag(request.question)

    return AnswerResponse(answer=answer)
