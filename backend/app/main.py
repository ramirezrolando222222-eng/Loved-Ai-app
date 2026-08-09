from fastapi import FastAPI

app = FastAPI(
    title="Loved AI API",
    description="AI-powered dating and social connection platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "Loved AI",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "loved-ai-api",
    }
