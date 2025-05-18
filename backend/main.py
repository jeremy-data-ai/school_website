from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def read_message():
    return {"message": "Hello from FastAPI"}


@app.get("/api/time")
def get_time():
    """Return the current server time in ISO format."""
    return {"time": datetime.utcnow().isoformat() + "Z"}
