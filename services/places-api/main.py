import os
import httpx
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Places API (Stateless)", version="1.0.0")

cors_origins = os.getenv("CORS_ORIGINS", "http://localhost:8080").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in cors_origins],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/search")
async def search(name: str = Query(..., min_length=1, description="City/place name")):
    params = {
        "name": name,
        "count": 5,
        "language": "tr",
        "format": "json",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(GEOCODE_URL, params=params)
        r.raise_for_status()
        data = r.json()

    # open-meteo "results" doğrudan dönüyor; stateless, DB yok.
    return {
        "query": name,
        "results": data.get("results", []) or [],
        "source": "geocoding-api.open-meteo.com",
    }
