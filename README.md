# Portfolio — kamalrathi.dev

Production-style personal portfolio: **React (Vite) + Tailwind + Framer Motion** frontend on `kamalrathi.dev`, **FastAPI + SQLite** API on `api.kamalrathi.dev` (SQLAlchemy URL can be pointed at PostgreSQL later if you want).

## Repository layout

| Path | Description |
|------|-------------|
| `backend/` | FastAPI app (`app/`), Alembic migrations, seed script |
| `frontend/` | Vite React SPA |

## Backend — run steps

1. Copy environment variables (default database is a local SQLite file):

   ```bash
   cd backend
   cp .env.example .env
   ```

   Edit `.env` with real `DATABASE_URL`, `API_KEY`, and SMTP settings.

2. Create a virtual environment and install dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   export PYTHONPATH=.
   alembic upgrade head
   ```

4. (Optional) Seed demo skills and a sample project:

   ```bash
   PYTHONPATH=. python scripts/seed.py
   ```

5. Run the API:

   ```bash
   PYTHONPATH=. uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   - Health: `GET http://localhost:8000/health`
   - OpenAPI: `http://localhost:8000/docs`

## Frontend — run steps

1. Configure the API base URL:

   ```bash
   cd frontend
   cp .env.example .env.local
   ```

   Prefer **`http://localhost:8000`** while developing (runs backend locally; avoids CORS). To call **`https://api.kamalrathi.dev`** from Vite on port 5173, deploy a backend build that includes the latest CORS logic: by default it **merges** `http://localhost:5173` (and a few other dev origins) into the allowlist unless **`CORS_STRICT=true`** in the API `.env`.

2. Install and run:

   ```bash
   npm install
   npm run dev
   ```

3. Production build:

   ```bash
   npm run build
   npm run preview
   ```

**CORS:** Production domains go in `CORS_ORIGINS`. Local Vite is covered automatically unless `CORS_STRICT=true`.

## API overview

| Method | Path | Auth | Notes |
|--------|------|------|--------|
| GET | `/health` | No | Liveness |
| GET | `/api/v1/projects` | No | Paginated list |
| POST | `/api/v1/projects` | Bearer `API_KEY` | Create project |
| GET | `/api/v1/skills` | No | Categorized skills |
| GET | `/api/v1/experience` | No | Work history (`items[]`) |
| POST | `/api/v1/contact` | No | Rate limit: **5 / 15 min / IP** |
| POST | `/api/v1/analytics/visit` | No | Optional page-visit beacon |

## Example `.env` (backend)

See `backend/.env.example`. Required variables:

- `DATABASE_URL` — SQLAlchemy URL (default `sqlite:///./portfolio.db`; use four slashes for absolute paths, e.g. `sqlite:////var/data/app.db`)
- `API_KEY` — value sent as `Authorization: Bearer <API_KEY>` for admin routes
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`
- Optional: `SMTP_FROM`, `CONTACT_NOTIFY_TO`, `CORS_ORIGINS`

## Example API requests

### POST `/api/v1/projects` (Bearer token)

```bash
curl -sS -X POST 'http://localhost:8000/api/v1/projects' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Payments service",
    "slug": "payments-service",
    "summary": "Idempotent payment intents and webhooks.",
    "description": "Detailed write-up for recruiters.",
    "tech_stack": ["FastAPI", "SQLite", "Redis"],
    "repo_url": "https://github.com/you/payments",
    "demo_url": null,
    "featured": true,
    "sort_order": 0
  }'
```

### POST `/api/v1/contact`

```bash
curl -sS -X POST 'http://localhost:8000/api/v1/contact' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Ada Lovelace",
    "email": "ada@example.com",
    "subject": "Backend role",
    "message": "I would like to discuss a backend engineering position.",
    "company": "Example Corp",
    "honeypot": null
  }'
```

### GET projects / skills

```bash
curl -sS 'http://localhost:8000/api/v1/projects'
curl -sS 'http://localhost:8000/api/v1/skills'
```

### Postman

- Create a request to `POST {{baseUrl}}/api/v1/projects`
- Authorization tab: Type **Bearer Token**, token = your `API_KEY`
- Body: raw JSON matching the schema above

## Design notes

- **Clean architecture**: routers → services → models; Pydantic schemas at the boundary.
- **Request logging**: middleware logs method, path, status, duration, and request id.
- **Errors**: centralized JSON shape `{ "error": { "code", "message", "request_id" } }`.
- **Contact**: row persisted, email sent via **SMTP** in a **BackgroundTasks** handler after `202 Accepted`.
