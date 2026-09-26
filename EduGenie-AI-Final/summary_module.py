from ai_client import generate_text


def summarize_text(text: str) -> str:
    text = text.strip()

    if not text:
        raise ValueError("Text cannot be empty.")

    prompt = f"""
You are EduGenie, an educational
summarization assistant.

Summarize the following educational text.

Requirements:
- Keep the important facts.
- Preserve important definitions.
- Preserve important relationships.
- Preserve conclusions.
- Remove repetition.
- Use simple language.
- Use bullet points when helpful.
- Do not add facts that are not present
  in the original text.

Educational text:

{text}
"""

    return generate_text(prompt)