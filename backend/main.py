from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import prod_engine, get_prod_db, qa_engine, get_qa_db
import models
import schemas
import db

# Create tables in Postgres if they do not exist
models.Base.metadata.create_all(bind=prod_engine)
models.Base.metadata.create_all(bind=qa_engine)

app = FastAPI(
    title="Share Info API", 
    description="API for Share Info application aimed at helping new grads.", 
    version="1.0.0"
)

# Configure CORS so the React frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Vite default dev server port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello World from FastAPI Backend!"}

@app.post("/upload-resume")
def upload_resume():
    return {"message": "Resume upload endpoint placeholder"}

# --- Database API Endpoints ---

@app.post("/prod/users/", response_model=schemas.UserResponse)
def create_user_endpoint(user: schemas.UserCreate, session: Session = Depends(get_prod_db)):
    return db.create_user(db=session, user=user)

@app.get("/prod/users/", response_model=list[schemas.UserResponse])
def get_users_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_prod_db)):
    return db.get_users(db=session, skip=skip, limit=limit)


@app.get("/prod/users/{user_id}", response_model=schemas.UserResponse)
def get_user_by_id_endpoint(user_id: int, session: Session = Depends(get_prod_db)):
    return db.get_user_by_id(db=session, user_id=user_id)

@app.get("/prod/users/{user_id}/all", response_model=schemas.UserAllInfoResponse)
def get_all_user_info_endpoint(user_id: int, session: Session = Depends(get_prod_db)):
    return db.get_all_user_info(db=session, user_id=user_id)


@app.get("/prod/users/email/{email}", response_model=schemas.UserResponse)
def get_user_by_email_endpoint(email: str, session: Session = Depends(get_prod_db)):
    return db.get_user_by_email(db=session, email=email)







@app.post("/qa/users/", response_model=schemas.UserResponse)
def create_user_endpoint(user: schemas.UserCreate, session: Session = Depends(get_qa_db)):
    return db.create_user(db=session, user=user)

@app.get("/qa/users/", response_model=list[schemas.UserResponse])
def get_users_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_qa_db)):
    return db.get_users(db=session, skip=skip, limit=limit)


@app.post("/prod/education/", response_model=schemas.EducationResponse)
def create_education_endpoint(education: schemas.EducationCreate, session: Session = Depends(get_prod_db)):
    return db.create_education(db=session, education=education)

@app.get("/prod/education/", response_model=list[schemas.EducationResponse])
def get_education_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_prod_db)):
    return db.get_education(db=session, skip=skip, limit=limit)

@app.post("/qa/education/", response_model=schemas.EducationResponse)
def create_education_endpoint(education: schemas.EducationCreate, session: Session = Depends(get_qa_db)):
    return db.create_education(db=session, education=education)

@app.get("/qa/education/", response_model=list[schemas.EducationResponse])
def get_education_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_qa_db)):
    return db.get_education(db=session, skip=skip, limit=limit)

@app.post("/prod/experience/", response_model=schemas.ExperienceResponse)
def create_experience_endpoint(experience: schemas.ExperienceCreate, session: Session = Depends(get_prod_db)):
    return db.create_experience(db=session, experience=experience)

@app.get("/prod/experience/", response_model=list[schemas.ExperienceResponse])
def get_experiences_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_prod_db)):
    return db.get_experiences(db=session, skip=skip, limit=limit)

@app.post("/qa/experience/", response_model=schemas.ExperienceResponse)
def create_experience_endpoint(experience: schemas.ExperienceCreate, session: Session = Depends(get_qa_db)):
    return db.create_experience(db=session, experience=experience)

@app.get("/qa/experience/", response_model=list[schemas.ExperienceResponse])
def get_experiences_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_qa_db)):
    return db.get_experiences(db=session, skip=skip, limit=limit)

@app.post("/prod/project/", response_model=schemas.ProjectResponse)
def create_project_endpoint(project: schemas.ProjectCreate, session: Session = Depends(get_prod_db)):
    return db.create_project(db=session, project=project)

@app.get("/prod/project/", response_model=list[schemas.ProjectResponse])
def get_projects_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_prod_db)):
    return db.get_projects(db=session, skip=skip, limit=limit)

@app.post("/qa/project/", response_model=schemas.ProjectResponse)
def create_project_endpoint(project: schemas.ProjectCreate, session: Session = Depends(get_qa_db)):
    return db.create_project(db=session, project=project)

@app.get("/qa/project/", response_model=list[schemas.ProjectResponse])
def get_projects_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_qa_db)):
    return db.get_projects(db=session, skip=skip, limit=limit)

@app.post("/prod/skill/", response_model=schemas.SkillResponse)
def create_skill_endpoint(skill: schemas.SkillCreate, session: Session = Depends(get_prod_db)):
    return db.create_skill(db=session, skill=skill)

@app.get("/prod/skill/", response_model=list[schemas.SkillResponse])
def get_skills_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_prod_db)):
    return db.get_skills(db=session, skip=skip, limit=limit)

@app.post("/qa/skill/", response_model=schemas.SkillResponse)
def create_skill_endpoint(skill: schemas.SkillCreate, session: Session = Depends(get_qa_db)):
    return db.create_skill(db=session, skill=skill)

@app.get("/qa/skill/", response_model=list[schemas.SkillResponse])
def get_skills_endpoint(skip: int = 0, limit: int = 100, session: Session = Depends(get_qa_db)):
    return db.get_skills(db=session, skip=skip, limit=limit)
