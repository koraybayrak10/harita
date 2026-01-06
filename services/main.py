from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# -----------------
# API'LER (ÖNCE!)
# -----------------

@app.get("/api/weather/current")
def current_weather(lat: float, lon: float):
    temp = round(20 + (lat % 10), 1)
    wind = round(5 + (lon % 8), 1)

    return {
        "location": {"lat": lat, "lon": lon},
        "weather": {
            "temperature": temp,
            "condition": "Değişken",
            "wind_kmh": wind,
            "humidity": int(40 + (lat % 30))
        }
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
