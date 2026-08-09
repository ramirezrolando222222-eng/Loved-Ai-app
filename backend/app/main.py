
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import (
    UserProfile,
    MatchRequest,
    ChatMessage,
    VideoCallRequest,
)


app = FastAPI(
    title="Loved AI API",
    description="AI-powered dating and social connection platform",
    version="0.2.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "name": "Loved AI",
        "status": "online",
        "version": "0.2.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "loved-ai-api",
    }


@app.post("/api/profiles")
async def create_profile(profile: UserProfile):
    return {
        "success": True,
        "profile": profile,
    }


@app.post("/api/matches")
async def create_match(request: MatchRequest):
    return {
        "success": True,
        "match": request,
        "message": "Match created",
    }


@app.post("/api/chat/messages")
async def send_message(message: ChatMessage):
    return {
        "success": True,
        "message": message,
    }


@app.post("/api/video/call")
async def start_video_call(request: VideoCallRequest):
    return {
        "success": True,
        "call": request,
        "status": "ready",
    }
