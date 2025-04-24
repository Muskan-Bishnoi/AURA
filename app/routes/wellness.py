from fastapi import APIRouter
from app.services.dna_parser import fetch_dna_traits
from app.services.emotion_ai import fetch_recent_emotions
from app.services.planner import generate_custom_plan
from fastapi import APIRouter
# from app.services.dna_parser import fetch_dna_traits
# from app.services.emotion_ai import fetch_recent_emotions
# from app.services.planner import generate_custom_plan  # hypothetical planner logic

router = APIRouter()

# @router.get("/get-wellness-plan/")
# async def get_plan(user_id: str):
#     # Fetch user traits from DNA
#     traits = fetch_dna_traits(user_id)
    
#     # Fetch recent emotions from the user logs
#     emotions = fetch_recent_emotions(user_id)
    
#     # Generate a wellness plan based on traits and emotions
#     plan = generate_custom_plan(traits, emotions)
#     return {"plan": plan}


@router.get("/get-wellness-plan/")
async def get_plan(user_id: str):
    # Mock values instead of calling the actual functions
    traits = {"energy_level": "high", "focus": "low"}
    emotions = ["anxious", "tired"]
    
    # Simulate the plan generation
    plan = {
        "morning": "20 min meditation",
        "afternoon": "light cardio",
        "evening": "read a book"
    }
    
    return {"plan": plan}


# router = APIRouter()
tasks_db = []

@router.get("/get-full-schedule/")
async def get_full_schedule(user_id: str):
    # 1. Fetch user-specific wellness plan
    traits = fetch_dna_traits(user_id)
    emotions = fetch_recent_emotions(user_id)
    wellness_plan = generate_custom_plan(traits, emotions)

    # 2. Fetch user's own tasks
    # user_tasks = [task for task in tasks_db if task.user_id == user_id]
    # user_tasks = [task for task in tasks_db if task["user_id"] == user_id]

    user_tasks = [task for task in tasks_db if task["user_id"] == user_id]

    # sorted_tasks = sorted(user_tasks, key=lambda x: x.time)
    sorted_tasks = sorted(user_tasks, key=lambda task: task["time"])


    # 3. Return combined result
    return {
        "user_id": user_id,
        "wellness_plan": wellness_plan,
        "personal_tasks": sorted_tasks
    }

