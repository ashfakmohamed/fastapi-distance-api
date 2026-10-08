# FastAPI Distance API

[![FastAPI CI](https://github.com/ashfakmohamed/fastapi-distance-api/actions/workflows/ci.yml/badge.svg)](https://github.com/ashfakmohamed/fastapi-distance-api/actions/workflows/ci.yml)

A FastAPI service that accepts two latitude/longitude pairs and returns their great-circle distance in kilometers using the haversine formula.

## Run locally

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Example

```text
GET /distance/?lat1=40.7128&lon1=-74.0060&lat2=34.0522&lon2=-118.2437
```

The API validates latitude and longitude ranges and exposes an OpenAPI schema at `/docs`.

## Tests

```bash
pip install -r requirements-dev.txt
pytest
```

## Repository hygiene

Generated virtual environments, caches, secrets, and local databases are excluded from version control. Install dependencies from `requirements.txt` instead of committing a local environment.
