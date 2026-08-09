from pydantic import BaseModel, Field
from typing import List, Optional


class UserProfile(BaseModel):
    id: str
    name: str
    age: int = Field(ge=18, le=120)
    location: Optional[str] = None
    bio: Optional[str] = None
    interests: List[str] = []
    profile_video_url: Optional[str] = None
    avatar_url: Optional[str] = None


class MatchRequest(BaseModel):
    user_id: str
    target_user_id: str


class ChatMessage(BaseModel):
    conversation_id: str
    sender_id: str
    text: str


class VideoCallRequest(BaseModel):
    caller_id: str
    receiver_id: str
