from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from pathlib import Path
import json
=======


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


DATA_DIR = Path(__file__).parent / "data"
MESSAGE_FILE = DATA_DIR / "message.json"
LLM_FILE = DATA_DIR / "llm_input.json"


def load_json(path: Path):
    if path.exists():
        with path.open() as f:
            return json.load(f)
    return {}


@app.get("/api/message")
def read_message():
    data = load_json(MESSAGE_FILE)
    return {"message": data.get("message", "Hello from FastAPI")}


@app.get("/api/llm-data")
def get_llm_data():
    return load_json(LLM_FILE)
=======
@app.get("/api/message")
def read_message():
    return {"message": "Hello from FastAPI"}



@app.get("/api/time")
def get_time():
    """Return the current server time in ISO format."""
    return {"time": datetime.utcnow().isoformat() + "Z"}

