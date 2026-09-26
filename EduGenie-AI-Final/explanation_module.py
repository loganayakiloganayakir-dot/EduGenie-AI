import os

from ai_client import generate_text


USE_LOCAL_EXPLANATION = (
    os.getenv("USE_LOCAL_EXPLANATION", "false").lower() == "true"
)


def _local_explain(topic: str) -> str:
    """
    Optional local explanation model.

    This is only used when USE_LOCAL_EXPLANATION=true.
    """

    from transformers import pipeline

    generator = pipeline(
        "text2text-generation",
        model="MBZUAI/LaMini-Flan-T5-783M",
    )

    prompt = f"""
Explain the following educational concept
in simple language for a beginner.

Use:
- simple terminology
- short paragraphs
- one small example

Concept:

{topic}
"""

    result = generator(
        prompt,
        max_new_tokens=220,
        do_sample=False,
    )

    return result[0]["generated_text"].strip()


def explain_concept(topic: str) -> str:
    """
    Explain an educational concept using Gemini
    or optionally the local explanation model.
    """

    topic = topic.strip()

    if not topic:
        raise ValueError("Topic cannot be empty.")

    # Optional local model
    if USE_LOCAL_EXPLANATION:

        try:
            return _local_explain(topic)

        except Exception as exc:
            print(
                "Local explanation model failed. "
                "Falling back to Gemini:",
                repr(exc),
            )

    # Gemini explanation
    prompt = f"""
You are EduGenie, an educational assistant.

Explain the following concept to a beginner.

Concept:
{topic}

Requirements:

1. Start with a simple definition.
2. Explain the main idea clearly.
3. Break the concept into smaller parts.
4. Use simple language.
5. Explain important terms.
6. Give a simple real-world example.
7. If there is a formula, explain what each part means.
8. Keep the explanation reasonably concise.
9. Do not invent facts.
"""

    return generate_text(prompt)