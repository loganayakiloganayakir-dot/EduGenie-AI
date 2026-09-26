import os
import time
from functools import lru_cache

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


MODEL_NAME = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash"
)

API_KEY = (
    os.getenv("GEMINI_API_KEY")
    or os.getenv("GOOGLE_API_KEY")
)


@lru_cache(maxsize=1)
def get_client():

    if not API_KEY:
        raise RuntimeError(
            "Gemini API key is missing. "
            "Set GEMINI_API_KEY in your .env file."
        )

    return genai.Client(
        api_key=API_KEY
    )


def generate_text(prompt: str) -> str:

    if not prompt or not prompt.strip():
        raise ValueError(
            "Prompt cannot be empty."
        )

    client = get_client()

    config = types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )

    last_error = None

    # Retry temporary Gemini 503 errors.
    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt.strip(),
                config=config,
            )

            text = getattr(
                response,
                "text",
                None
            )

            if not text:
                raise RuntimeError(
                    "Gemini returned an empty response."
                )

            return text.strip()

        except Exception as exc:

            last_error = exc

            error_text = str(exc)

            # Retry only temporary availability/rate-limit errors.
            if (
                "503" in error_text
                or "UNAVAILABLE" in error_text
                or "429" in error_text
                or "RESOURCE_EXHAUSTED" in error_text
            ):

                if attempt < 2:

                    wait_seconds = 2 ** attempt

                    print(
                        f"Gemini temporarily unavailable. "
                        f"Retrying in {wait_seconds} seconds..."
                    )

                    time.sleep(
                        wait_seconds
                    )

                    continue

            raise

    raise RuntimeError(
        f"Gemini request failed after retries: {last_error}"
    )