export DATABASE_ENVIRONMENT=prod
source venv/bin/activate
uvicorn main:app --reload
