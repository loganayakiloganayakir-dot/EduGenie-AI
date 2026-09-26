from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


# ---------------------------------------------------------
# Basic API tests
# ---------------------------------------------------------

def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "EduGenie"


def test_home_page():
    response = client.get("/")

    assert response.status_code == 200
    assert "EduGenie" in response.text


# ---------------------------------------------------------
# Validation tests
# ---------------------------------------------------------

def test_qa_validation():
    response = client.post(
        "/qa",
        json={"text": ""}
    )

    assert response.status_code == 422


def test_explain_validation():
    response = client.post(
        "/explain",
        json={"text": ""}
    )

    assert response.status_code == 422


def test_quiz_validation():
    response = client.post(
        "/quiz",
        json={"text": ""}
    )

    assert response.status_code == 422


def test_summary_validation():
    response = client.post(
        "/summarize",
        json={"text": ""}
    )

    assert response.status_code == 422


def test_recommendations_validation():
    response = client.post(
        "/learn/recommendations",
        json={"text": ""}
    )

    assert response.status_code == 422


# ---------------------------------------------------------
# AI endpoint tests
# ---------------------------------------------------------

def test_qa_ai_endpoint():
    with patch(
        "qna.generate_text",
        return_value=(
            "Photosynthesis is the process plants use "
            "to make food using sunlight."
        )
    ):
        response = client.post(
            "/qa",
            json={"text": "What is photosynthesis?"}
        )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert isinstance(data["answer"], str)
    assert len(data["answer"].strip()) > 0


def test_explain_ai_endpoint():
    with patch(
        "explanation_module.generate_text",
        return_value=(
            "Gravity is the force that pulls "
            "objects toward each other."
        )
    ):
        response = client.post(
            "/explain",
            json={"text": "Explain gravity to a beginner."}
        )

    assert response.status_code == 200

    data = response.json()

    assert "explanation" in data
    assert isinstance(data["explanation"], str)
    assert len(data["explanation"].strip()) > 0


def test_quiz_ai_endpoint():
    fake_quiz = """
[
    {
        "question": "What is Python?",
        "options": [
            "A programming language",
            "A database",
            "An operating system",
            "A web browser"
        ],
        "answer": "A programming language"
    },
    {
        "question": "Which symbol starts a Python comment?",
        "options": [
            "#",
            "//",
            "/*",
            "<!--"
        ],
        "answer": "#"
    },
    {
        "question": "Which function displays text in Python?",
        "options": [
            "print()",
            "displayText()",
            "show()",
            "writeText()"
        ],
        "answer": "print()"
    }
]
"""

    with patch(
        "quiz_module.generate_text",
        return_value=fake_quiz
    ):
        response = client.post(
            "/quiz",
            json={"text": "Basic Python programming"}
        )

    assert response.status_code == 200

    data = response.json()

    assert "quiz" in data
    assert isinstance(data["quiz"], list)
    assert len(data["quiz"]) == 3

    for question in data["quiz"]:
        assert "question" in question
        assert "options" in question
        assert "answer" in question

        assert isinstance(question["options"], list)
        assert len(question["options"]) == 4
        assert question["answer"] in question["options"]


def test_summary_ai_endpoint():
    with patch(
        "summary_module.generate_text",
        return_value=(
            "Plants use sunlight, water, and carbon dioxide "
            "to produce glucose and oxygen."
        )
    ):
        response = client.post(
            "/summarize",
            json={
                "text": (
                    "Photosynthesis is the process by which "
                    "green plants use sunlight, water, and carbon dioxide "
                    "to produce glucose and oxygen."
                )
            }
        )

    assert response.status_code == 200

    data = response.json()

    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"].strip()) > 0


def test_recommendations_ai_endpoint():
    with patch(
        "learning_path.generate_text",
        return_value=(
            "Beginner: Learn Python syntax and variables.\n"
            "Intermediate: Build small Python projects.\n"
            "Advanced: Study algorithms and software architecture."
        )
    ):
        response = client.post(
            "/learn/recommendations",
            json={"text": "Python programming for beginners"}
        )

    assert response.status_code == 200

    data = response.json()

    assert "recommendations" in data
    assert isinstance(data["recommendations"], str)
    assert len(data["recommendations"].strip()) > 0