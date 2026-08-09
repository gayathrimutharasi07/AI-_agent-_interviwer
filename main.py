import json
from pathlib import Path
import os

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

BASE_DIR = Path(__file__).resolve().parent
CURRICULUM_FILE = BASE_DIR / "curriculum.json"

with open(CURRICULUM_FILE, "r", encoding="utf-8") as file:
    curriculum = json.load(file)

app = FastAPI(
    title="AI Interview Agent",
    description="An adaptive AI technical interviewer",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


from fastapi.responses import FileResponse

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

@app.get("/")
def home():
    return {
        "message": "AI Interview Agent backend is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/curriculum")
def get_curriculum():
    return curriculum


class InterviewRequest(BaseModel):
    candidate_name: str
    role: str


@app.post("/start-interview")
def start_interview(request: InterviewRequest):
    return {
        "message": "Interview started successfully",
        "candidate_name": request.candidate_name,
        "role": request.role,
        "question": "Tell me about yourself and your technical background."
    }


class QuestionRequest(BaseModel):
    track: str
    level: str
    topic: str


@app.post("/generate-question")
def generate_question(request: QuestionRequest):

    prompt = f"""
You are a friendly and professional human interviewer.

Conduct a realistic interview for a candidate.

Track: {request.track}
Level: {request.level}
Topic: {request.topic}

Generate ONE interview question.

Requirements:
- Make it sound natural and human, not robotic.
- Match the candidate's level.
- Keep it clear and concise.
- Do not provide the answer.
- Do not number the question.
- Avoid generic textbook wording.
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return {
        "question": response.text.strip()
    }