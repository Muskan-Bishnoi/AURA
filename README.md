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

AURA/ 
├── app/
│ ├── main.py # FastAPI entry point 
│ ├── routes/
│ │ ├── tasks.py # Task creation & fetching 
│ │ ├── wellness.py # Wellness creation & full schedule logic
│ └── models/ 
│   ├── task_model.py # Task schemas 
│   └── wellness_model.py # Wellness schemas 
├── .gitignore 
├── requirements.txt 
└── README.md
