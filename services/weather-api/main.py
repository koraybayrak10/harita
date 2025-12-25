import os
import httpx
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Weather API (Stateless)", version="1.0.0")

cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:8080").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in cors_origins],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/current")
async def current(
    lat: float = Query(..., ge=-90, le=90),
    lon: float = Query(..., ge=-180, le=180),
):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m",
        "timezone": "auto",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(FORECAST_URL, params=params)
        try:
            r.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=502, detail=f"Upstream error: {e}")

        data = r.json()

    cur = data.get("current") or {}
    return {
        "coords": {"lat": lat, "lon": lon},
        "time": cur.get("time"),
        "temperature_c": cur.get("temperature_2m"),
        "feels_like_c": cur.get("apparent_temperature"),
        "humidity_percent": cur.get("relative_humidity_2m"),
        "wind_kmh": cur.get("wind_speed_10m"),
        "source": "api.open-meteo.com",
    }
