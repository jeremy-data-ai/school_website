# School Website

This repository contains a minimal example of a React frontend and FastAPI backend.
The frontend uses Tailwind CSS for styling. The backend exposes a JSON API
that the frontend consumes.

## Requirements
- Node.js and npm (for the frontend)
- Python 3.11 (for the backend)
- Docker and docker-compose (optional)

## Running with Docker
To start both the backend and frontend using Docker:

```bash
docker-compose up --build
```

The frontend will be available at http://localhost:3000 and the backend at
http://localhost:8000.

## Running manually

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

The frontend development server will proxy API requests to the backend if you
configure a proxy or adjust the fetch URL accordingly.

## Project structure

- `frontend/` React application using Tailwind CSS. Components live in `src/components` and API helpers in `src/api.js`.
- `backend/` FastAPI service serving JSON from files in `backend/data`.

### Example JSON files

The backend loads data from `backend/data/message.json` and `backend/data/llm_input.json`. These files can be modified to integrate with an LLM or transformer model in the future.
