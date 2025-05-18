# School Website

This repository contains a minimal example of a React frontend, a Next.js
frontend, and a FastAPI backend. The React app uses Tailwind CSS for styling.
The Next.js app demonstrates server-side rendering. Both frontends consume the
JSON API exposed by the backend.

The API now includes an additional `/api/time` endpoint that returns the
current server time in ISO format. The frontend displays this value on load.

## Requirements
- Node.js and npm (for the frontend)
- Python 3.11 (for the backend)
- Docker and docker-compose (optional)

## Running with Docker
To start the backend, React frontend and Next.js frontend using Docker:

```bash
docker-compose up --build
```

The React app will be available at http://localhost:3000, the Next.js app at
http://localhost:3001 and the backend at http://localhost:8000.

## Running manually

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

To run the backend tests:

```bash
python -m unittest
```

### Frontend
```bash
cd frontend
npm install
npm start
```


### Next.js Frontend
```bash
cd nextjs
npm install
npm run dev
```

The development servers for the frontends can proxy API requests to the backend
if you configure a proxy or adjust the fetch URLs accordingly.

The frontend development server will proxy API requests to the backend if you
configure a proxy or adjust the fetch URL accordingly.


## Project structure

- `frontend/` React application using Tailwind CSS. Components live in `src/components` and API helpers in `src/api.js`.
- `backend/` FastAPI service serving JSON from files in `backend/data`.

### Example JSON files

The backend loads data from `backend/data/message.json` and `backend/data/llm_input.json`. These files can be modified to integrate with an LLM or transformer model in the future.

