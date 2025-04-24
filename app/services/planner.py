# app/services/planner.py

from typing import Dict, List

def generate_custom_plan(traits: Dict[str, str], emotions: List[str]) -> Dict[str, str]:
    plan = {}

    # Sample logic based on traits
    if traits.get("energy_level") == "low":
        plan["morning"] = "Sunlight exposure + light stretching"
    else:
        plan["morning"] = "Yoga or brisk walk"

    if traits.get("focus") == "low":
        plan["afternoon"] = "Pomodoro session + green tea"
    else:
        plan["afternoon"] = "Deep work session"

    # Sample logic based on recent emotions
    if "anxious" in emotions or "stressed" in emotions:
        plan["evening"] = "Guided meditation + journaling"
    elif "tired" in emotions:
        plan["evening"] = "Early sleep + calming music"
    else:
        plan["evening"] = "Free time or hobby activity"

    return plan
