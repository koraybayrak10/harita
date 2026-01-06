from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount(
    "/",
    StaticFiles(directory="../frontend", html=True),
    name="frontend"
)

@app.get("/api/health")
def health():
    return {"status": "ok"}
