from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS (frontend için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Frontend'i servis et
app.mount(
    "/", 
    StaticFiles(directory="frontend", html=True), 
    name="frontend"
)

# TEST endpoint
@app.get("/api/health")
def health():
    return {"status": "ok"}
