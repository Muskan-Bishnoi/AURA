from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.emotion_ai import fetch_recent_emotions
from typing import Literal

router = APIRouter()

class EmotionLog(BaseModel):
    user_id: str
    primary_emotion: Literal[
        "joy", "sadness", "anger", "fear", "disgust", "surprise",
        "trust", "anticipation", "love", "shame", "guilt", "envy",
        "pride", "grief", "embarrassment", "boredom", "awe", "relief"
    ]
    intensity: Literal[
        "very low", "low", "medium", "high", "very high"
    ]
    energy: Literal[
        "very low", "low", "neutral", "high", "very high"
    ]
    mood_stability: Literal[
        "very unstable", "unstable", "neutral", "stable", "very stable"
    ]
    context: Literal[
        "personal", "work", "social", "health", "financial", "relationship", "unknown"
    ]
    additional_notes: str = ""  # Optional field

@router.post("/submit-emotion/")
async def submit_emotion(emotion_data: EmotionLog):
    # Save the emotion data to the database or process it accordingly
    try:
        # Example: Process the emotion data and store in a database
        print(f"Emotion data received: {emotion_data.dict()}")
        
        # If successfully processed, return a success message
        return {"message": "Emotion data submitted successfully"}
    
    except Exception as e:
        # Handle any errors that may occur
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
