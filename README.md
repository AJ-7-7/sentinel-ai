# SentinelAI

SentinelAI is an in-development financial fraud detection
and investigation platform.

## Project Goals

- Build a secure transaction processing API
- Detect suspicious financial activity
- Generate risk scores and fraud alerts
- Provide investigation workflows
- Deploy and monitor the application on AWS

## Technology Stack

- Python
- FastAPI
- PostgreSQL (planned)
- React (planned)
- AWS (planned)

## Current Status

Initial FastAPI application with root and health-check endpoints.

## Local Development

Create and activate a Python virtual environment,
install FastAPI, and run:

```bash
python -m uvicorn app.main:app --reload
```

Interactive API documentation:
http://127.0.0.1:8000/docs