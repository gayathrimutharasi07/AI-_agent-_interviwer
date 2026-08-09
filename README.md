AI Interview Agent

An AI-powered technical interview platform designed to simulate a realistic human interviewer. The system generates interview questions based on the selected interview track, difficulty level, and topic.

Features
AI-generated technical interview questions
Humanized interview experience
Track-based interviews
Difficulty-level selection
Topic-based questions
Gemini AI integration
FastAPI backend
Interactive web frontend
Question-generation fallback
Technology Stack
Frontend: HTML, CSS, JavaScript
Backend: Python, FastAPI
AI: Google Gemini API
Server: Uvicorn
Project Structure
AI-Interview-Agent/
└── backend/
    ├── main.py
    ├── curriculum.json
    ├── requirements.txt
    └── frontend/
        └── index.html


Running the Project
Backend
cd backend
python -m uvicorn main:app --reload --port 8000


Frontend

Open another terminal:

cd backend/frontend
python -m http.server 5500



Then open:

https://ai-agent-interviwer-4.onrender.com


Gemini API Configuration

Create a .env file inside the backend directory:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY



Never upload the actual API key to the public repository.

Project Objective

The objective of AI Interview Agent is to provide candidates with an accessible and realistic technical interview practice environment using generative AI.

Future Enhancements
Voice-based interviews
Resume-based questioning
Automated candidate scoring
Performance analytics
Adaptive interview difficulty
Interview reports
Competition Project
