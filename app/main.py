from fastapi import FastAPI
from app.api.transactions import router as transactions_router

app = FastAPI(
    title="SentinelAI",
    description="Intelligent Fraud Detection and Investigation Platform",
    version="0.1.0",
)

app.include_router(transactions_router)

@app.get("/")
def home():
    return {
        "project": "SentinelAI",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }