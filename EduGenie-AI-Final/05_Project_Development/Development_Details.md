# Project Development

## 1. Project Name

EduGenie - AI-Powered Learning Assistant

## 2. Development Overview

EduGenie was developed as a web-based Generative AI application.

The application combines a browser-based frontend, FastAPI backend,
feature-specific Python modules, and Google Gemini AI integration.

## 3. Backend Development

The backend is implemented using FastAPI.

The main application file is:

`main.py`

The backend exposes API endpoints for the major learning features.

## 4. AI Client Development

The AI communication is separated into:

`ai_client.py`

The module is responsible for interacting with the configured
Google Gemini service.

The API key is read from an environment variable.

## 5. Q&A Development

The Q&A functionality is implemented in:

`qna.py`

It receives a user question and produces an AI-generated educational
answer.

## 6. Concept Explanation Development

The concept explanation functionality is implemented in:

`explanation_module.py`

It is designed to produce simple explanations of educational concepts.

## 7. Quiz Development

Quiz generation is implemented in:

`quiz_module.py`

The module generates educational multiple-choice questions based on
the requested topic.

## 8. Summarization Development

Text summarization is implemented in:

`summary_module.py`

The module processes the provided educational content and generates
a concise summary.

## 9. Learning Path Development

Learning recommendations are implemented in:

`learning_path.py`

The module generates structured learning recommendations based on
the selected topic.

## 10. Frontend Development

The frontend is implemented using:

- HTML
- CSS
- JavaScript

The frontend allows users to select a learning task and submit
information to the appropriate backend endpoint.

## 11. API Documentation

FastAPI automatically provides interactive API documentation at:

`/docs`

For local development, the documentation can be accessed through:

`http://127.0.0.1:8002/docs`

## 12. Configuration

The project uses environment variables for sensitive configuration.

A `.env.example` file is included as a configuration reference.

The actual `.env` file is not intended to be committed to the public
repository.

## 13. Dependencies

Project dependencies are specified in:

`requirements.txt`

## 14. Running the Application

Install dependencies:

```bash
pip install -r requirements.txt