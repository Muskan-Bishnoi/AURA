from pydantic import BaseModel
from typing import Literal

class EmotionLog(BaseModel):
    user_id: str
    timestamp: str  # e.g., ISO datetime string or date

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

    additional_notes: str = ""  # Optional field to add any extra context for emotions
