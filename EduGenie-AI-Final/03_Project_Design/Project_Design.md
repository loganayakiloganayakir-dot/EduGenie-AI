# Project Design

## 1. System Architecture

EduGenie follows a client-server architecture.

```text
+-----------------------+
|        Student        |
+-----------+-----------+
            |
            v
+-----------------------+
|    Web Frontend       |
| HTML / CSS / JS       |
+-----------+-----------+
            |
            v
+-----------------------+
|     FastAPI Backend   |
+-----------+-----------+
            |
     +------+------+
     |      |      |
     v      v      v
   Q&A  Explanation Quiz
     |      |      |
     +------+------+
            |
     +------+------+
     |             |
     v             v
 Summary      Learning Path
     |             |
     +------+------+
            |
            v
+-----------------------+
|   AI Client Module    |
+-----------+-----------+
            |
            v
+-----------------------+
|    Google Gemini     |
|    Generative AI     |
+-----------+-----------+
            |
            v
+-----------------------+
|    AI Generated       |
|       Response        |
+-----------+-----------+
            |
            v
+-----------------------+
|      Frontend         |
+-----------------------+