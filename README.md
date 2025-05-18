# School Website

This repository contains a minimal example of a React frontend, a Next.js
frontend, and a FastAPI backend. The React app uses Tailwind CSS for styling.
The Next.js app demonstrates server-side rendering. Both frontends consume the
JSON API exposed by the backend.

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
