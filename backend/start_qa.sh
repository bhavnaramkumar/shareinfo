export DATABASE_ENVIRONMENT=qa
source venv/bin/activate
uvicorn main:app --reload --port 8000

