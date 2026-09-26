from ai_client import generate_text


def get_learning_recommendations(topic: str) -> str:
    topic = topic.strip()

    if not topic:
        raise ValueError("Topic cannot be empty.")

    prompt = f"""
You are EduGenie, an educational
learning-path assistant.

Create a structured learning path for:

{topic}

Organize the path into:

1. Beginner
2. Intermediate
3. Advanced

For every stage provide:

- Concepts to learn
- Practical activity
- Suggested resource types
- Expected learning outcome

Make the progression realistic.

Possible resource types include:

- Documentation
- Tutorials
- Videos
- Articles
- Books
- Practice projects

Do not invent specific URLs.

Keep the plan clear and practical.
"""

    return generate_text(prompt)