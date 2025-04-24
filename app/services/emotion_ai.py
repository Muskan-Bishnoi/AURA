import whisper
from transformers import pipeline

# Load models once
whisper_model = whisper.load_model("base")  # or "tiny" for faster results
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=False)

def whisper_to_text(audio_file_path: str) -> str:
    result = whisper_model.transcribe(audio_file_path)
    return result["text"]

def predict_emotion(text: str) -> str:
    emotion = emotion_model(text)[0]['label']
    return emotion

# app/services/emotion_ai.py

def fetch_recent_emotions(user_id: str):
    # Sample implementation, make sure this logic exists
    # You can fetch emotions from a database or an AI model
    return {"emotion": "joy", "intensity": "high", "energy": "medium", "context": "personal"}

