from ai_client import generate_text


def answer_question(question: str) -> str:
    question = question.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    prompt = f"""
You are EduGenie, a helpful educational
question-and-answer assistant.

Answer the student's question accurately
and clearly.

Rules:

1. Use simple language.
2. Explain difficult terms.
3. Give a short example when useful.
4. Avoid unnecessary jargon.
5. If the question is ambiguous, clearly
   state the assumption you are making.
6. Do not invent facts.

Student question:

{question}
"""

    return generate_text(prompt)