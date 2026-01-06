from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# -----------------
# API'LER (ÖNCE!)
# -----------------

@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/places/search")
def search_place(name: str = Query(...)):
    return {
        "results": [
            {
                "name": name.title(),
                "latitude": 41.0082,
                "longitude": 28.9784
            }
        ]
    }

@app.get("/api/weather/current")
def current_weather(lat: float, lon: float):
    return {
        "location": {"lat": lat, "lon": lon},
        "weather": {
            "temperature": 23,
            "condition": "Parçalı Bulutlu",
            "wind_kmh": 12,
            "humidity": 58
        }
    }

# -----------------
# FRONTEND (EN SON!)
# -----------------

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount(
    "/",
    StaticFiles(directory=str(FRONTEND_DIR), html=True),
    name="frontend"
)
