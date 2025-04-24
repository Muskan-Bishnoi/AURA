# 🌟 AURA – Your Personal Wellness & Productivity Assistant

AURA is an AI-powered scheduling tool that blends **task management** with **wellness goals** to help users maintain a balanced life. Users can create tasks, set wellness routines, and get personalized schedules—all intelligently merged.

---

## 🚀 Features

- ✅ Add custom tasks (meetings, classes, personal tasks, etc.)
- 💆 Schedule personalized wellness routines (e.g., meditation, yoga, journaling)
- 🧠 AI-powered logic to create an optimal **combined daily schedule**
- 🔐 User-specific data separation via `user_id`
- ⚙️ Built with **FastAPI** and **Pydantic**

---

## 🗂 Project Structure

aura_project/
│
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── routes/
│   │   ├── dna.py           # Upload & parse genetic data
│   │   ├── emotions.py      # Upload voice/text & analyze emotion
│   │   ├── wellness.py      # Generate recommendations
│   ├── services/
│   │   ├── dna_parser.py    # Extract traits from DNA (CSV)
│   │   ├── emotion_ai.py    # Emotion detection using models
│   │   ├── planner.py       # Adaptive suggestion engine
│   ├── models/
│   │   └── schemas.py       # Pydantic models
│   ├── database/
│   │   └── db.py            # DB connection
│   └── utils/
│       └── logger.py        # Optional: for logging/debugging
│
├── data/
│   ├── example_dna.csv      # Sample 23andMe file
│   └── emotion_logs.json    # User emotion logs (text/audio info)
│
├── requirements.txt
└── README.md


