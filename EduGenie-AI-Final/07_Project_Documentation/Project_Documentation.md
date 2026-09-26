# Project Documentation

# EduGenie - AI-Powered Learning Assistant

## 1. Project Overview

EduGenie is a Generative AI-powered educational assistant designed
to support students with interactive learning tasks.

The application uses Google Gemini to provide AI-generated educational
responses.

## 2. Project Objectives

The main objectives are:

- Provide immediate educational question answering.
- Explain concepts in simple language.
- Generate practice quizzes.
- Summarize educational content.
- Provide structured learning recommendations.

## 3. Major Features

### Question Answering

Allows users to ask educational questions.

### Concept Explanation

Provides simple explanations of difficult concepts.

### Quiz Generation

Generates multiple-choice questions for selected topics.

### Text Summarization

Produces concise summaries from longer educational content.

### Learning Path

Generates structured recommendations for learning a selected topic.

## 4. Technology Stack

- Python
- FastAPI
- Uvicorn
- Google Gemini
- HTML
- CSS
- JavaScript
- Pytest

## 5. Application Architecture

The frontend communicates with the FastAPI backend.

The backend uses separate modules for the different learning features
and communicates with Google Gemini through the AI client.

## 6. Installation

Create a Python virtual environment:

```bash
python -m venv .venv