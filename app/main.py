from fastapi import FastAPI
from app.routes import dna, emotion, wellness, task
from app.routes import emotion



app = FastAPI(title="AURA: Adaptive Understanding through RNA-based AI")

# Register the routes with FastAPI
app.include_router(dna.router, prefix="/dna", tags=["DNA"])
app.include_router(emotion.router, prefix="/emotion", tags=["Emotion"])
app.include_router(emotion.router, prefix="/emotion", tags=["Emotion"])
app.include_router(wellness.router, prefix="/wellness", tags=["Wellness"])
app.include_router(task.router, prefix = "/task", tags = ["Task"])
