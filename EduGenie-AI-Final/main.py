from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from explanation_module import explain_concept
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(
    title="EduGenie - AI Learning Assistant",
    version="1.0.0",
    description="AI-powered educational assistant using Google Gemini.",
)


# ---------------------------------------------------------
# Static files and templates
# ---------------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)

templates = Jinja2Templates(
    directory="templates"
)


# ---------------------------------------------------------
# Request model
# ---------------------------------------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=30000,
    )


# ---------------------------------------------------------
# Homepage
# ---------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
    )


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie",
    }


# ---------------------------------------------------------
# Question and Answer
# ---------------------------------------------------------

@app.post("/qa")
async def qa(payload: TextRequest):

    try:

        answer = answer_question(
            payload.text
        )

        return {
            "answer": answer
        }

    except Exception as exc:

        print("QA ERROR:", repr(exc))

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


# ---------------------------------------------------------
# Explain Concept
# ---------------------------------------------------------

@app.post("/explain")
async def explain(payload: TextRequest):

    try:

        explanation = explain_concept(
            payload.text
        )

        return {
            "explanation": explanation
        }

    except Exception as exc:

        print("EXPLAIN ERROR:", repr(exc))

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


# ---------------------------------------------------------
# Generate Quiz
# ---------------------------------------------------------

@app.post("/quiz")
async def quiz(payload: TextRequest):

    try:

        quiz = generate_quiz(
            payload.text
        )

        return {
            "quiz": quiz
        }

    except Exception as exc:

        print("QUIZ ERROR:", repr(exc))

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


# ---------------------------------------------------------
# Summarize
# ---------------------------------------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):

    try:

        summary = summarize_text(
            payload.text
        )

        return {
            "summary": summary
        }

    except Exception as exc:

        print("SUMMARY ERROR:", repr(exc))

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


# ---------------------------------------------------------
# Learning Recommendations
# ---------------------------------------------------------

@app.post("/learn/recommendations")
async def recommendations(payload: TextRequest):

    try:

        recommendations = get_learning_recommendations(
            payload.text
        )

        return {
            "recommendations": recommendations
        }

    except Exception as exc:

        print("RECOMMENDATIONS ERROR:", repr(exc))

        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )