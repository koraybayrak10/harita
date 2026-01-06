from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (front ayrı/aynı fark etmez)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent  # /app
FRONTEND_DIR = BASE_DIR / "frontend"               # /app/frontend

# Frontend'i kökten servis et (http://localhost:8000)
app.mount("/", StaticFiles(directory=str(FRONTEND_DIR), html=True), name="frontend")

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Not: kendi /api/places ve /api/weather endpointlerin varsa buraya ekleyeceksin
