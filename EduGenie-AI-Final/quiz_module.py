import json
import re
from typing import Any

from ai_client import generate_text


def clean_json_block(text: str) -> str:
    text = text.strip()

    text = re.sub(
        r"^```(?:json)?\s*",
        "",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\s*```$",
        "",
        text,
    )

    return text.strip()


def _validate_quiz(data: Any) -> list[dict]:
    if not isinstance(data, list):
        raise ValueError("Quiz response must be a JSON list.")

    validated = []

    for item in data[:3]:
        if not isinstance(item, dict):
            raise ValueError(
                "Each quiz question must be an object."
            )

        question = str(
            item.get("question", "")
        ).strip()

        options = item.get("options", [])

        answer = str(
            item.get("answer", "")
        ).strip()

        if (
            not question
            or not isinstance(options, list)
            or len(options) != 4
            or not answer
        ):
            raise ValueError(
                "Each question requires a question, "
                "four options, and an answer."
            )

        options = [
            str(option).strip()
            for option in options
        ]

        if any(not option for option in options):
            raise ValueError(
                "Quiz options cannot be empty."
            )

        if answer not in options:
            if answer.isdigit() and 0 <= int(answer) < 4:
                answer = options[int(answer)]
            else:
                raise ValueError(
                    "Answer must match one of the options."
                )

        validated.append(
            {
                "question": question,
                "options": options,
                "answer": answer,
            }
        )

    if len(validated) != 3:
        raise ValueError(
            "Gemini must return exactly three questions."
        )

    return validated


def generate_quiz(text: str) -> list[dict]:
    text = text.strip()

    if not text:
        raise ValueError(
            "Topic or passage cannot be empty."
        )

    prompt = f"""
Generate exactly THREE multiple-choice
questions from the educational topic
or passage below.

Each question must contain:

- question
- exactly four options
- correct answer

The answer must exactly match
one of the options.

Return ONLY valid JSON.
Do not use Markdown.
Do not add explanations.

Use exactly this format:

[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "answer": "Option A"
  }}
]

Educational source:

{text}
"""

    raw = generate_text(prompt)

    cleaned = clean_json_block(raw)

    try:
        data = json.loads(cleaned)

    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Gemini returned invalid quiz JSON: {exc}"
        ) from exc

    return _validate_quiz(data)