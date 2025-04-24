from pydantic import BaseModel, Field
from typing import Literal

class DNATraits(BaseModel):
    user_id: str

    # Core Traits
    energy_level: Literal[
        "very low", "low", "moderate", "high", "very high"
    ]
    focus: Literal[
        "very low", "low", "average", "high", "very high"
    ]
    sleep_quality: Literal[
        "very poor", "poor", "average", "good", "excellent"
    ]
    caffeine_sensitivity: Literal[
        "none", "low", "moderate", "high", "extreme"
    ]
    stress_response: Literal[
        "very calm", "calm", "moderate", "reactive", "very reactive"
    ]
    chronotype: Literal[
        "extreme morning", "morning", "neutral", "evening", "extreme evening"
    ]

    # New Advanced Traits
    appetite_regulation: Literal[
        "very low", "low", "balanced", "high", "uncontrolled"
    ]
    hydration_needs: Literal[
        "very low", "low", "average", "high", "very high"
    ]
    exercise_recovery_speed: Literal[
        "very slow", "slow", "moderate", "fast", "very fast"
    ]
    nutrient_absorption_efficiency: Literal[
        "very poor", "poor", "average", "good", "excellent"
    ]
