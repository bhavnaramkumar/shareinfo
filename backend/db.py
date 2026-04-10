import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
import models
import schemas

# 2. Get the logger inside db.py
logger = logging.getLogger(__name__)

def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user in the PostgreSQL database.
    """
    logger.info(f"Attempting to create user with email: {user.email}") # INFO log
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        logger.info(f"Successfully created user with ID: {db_user.id}") # INFO log
        return db_user
    except IntegrityError:
        db.rollback()
        logger.error(f"Failed to create user. Email {user.email} is already registered.") # ERROR log
        raise HTTPException(status_code=400, detail="Email is already registered")

def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of users from the PostgreSQL database.
    """
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    """
    Retrieve a list of users from the PostgreSQL database.
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_education(db: Session, education: schemas.EducationCreate):
    """
    Create a new education in the PostgreSQL database.
    """
    db_education = models.Education(**education.model_dump())
    db.add(db_education)
    try:
        db.commit()
        db.refresh(db_college)
        return db_college
    except IntegrityError as e:
        db.rollback()
        error_msg = str(e)
        if "ForeignKeyViolation" in error_msg:
            friendly_msg = "The specified user does not exist. Please create the user first."
        elif "UniqueViolation" in error_msg:
            friendly_msg = "You have already registered this combination of college, major, and minor."
        else:
            friendly_msg = "A database error occurred while registering the college."
            
        raise HTTPException(status_code=400, detail=friendly_msg)

def get_education(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of education from the PostgreSQL database.
    """
    return db.query(models.Education).offset(skip).limit(limit).all()     

def create_experience(db: Session, experience: schemas.ExperienceCreate):
    """
    Create a new experience in the PostgreSQL database.
    """
    db_experience = models.Experience(**experience.model_dump())
    db.add(db_experience)
    try:
        db.commit()
        db.refresh(db_experience)
        return db_experience
    except IntegrityError as e:
        db.rollback()
        error_msg = str(e)
        if "ForeignKeyViolation" in error_msg:
            friendly_msg = "The specified user does not exist. Please create the user first."
        elif "UniqueViolation" in error_msg:
            friendly_msg = "You have already registered this combination of work place, job title and location."
        else:
            friendly_msg = "A database error occurred while registering the experience."
            
        raise HTTPException(status_code=400, detail=friendly_msg)

def get_experience(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of experiences from the PostgreSQL database.
    """
    return db.query(models.Experience).offset(skip).limit(limit).all()     

def create_project(db: Session, project: schemas.ProjectCreate):
    """
    Create a new project in the PostgreSQL database.
    """
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    try:
        db.commit()
        db.refresh(db_project)
        return db_project
    except IntegrityError as e:
        db.rollback()
        error_msg = str(e)
        if "ForeignKeyViolation" in error_msg:
            friendly_msg = "The specified user does not exist. Please create the user first."
        elif "UniqueViolation" in error_msg:
            friendly_msg = "You have already registered this project."
        else:
            friendly_msg = "A database error occurred while registering the project."
            
        raise HTTPException(status_code=400, detail=friendly_msg)

def get_project(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of projects from the PostgreSQL database.
    """
    return db.query(models.Project).offset(skip).limit(limit).all()     

def create_skill(db: Session, skill: schemas.SkillCreate):
    """
    Create a new skill in the PostgreSQL database.
    """
    db_skill = models.Skill(**skill.model_dump())
    db.add(db_skill)
    try:
        db.commit()
        db.refresh(db_skill)
        return db_skill
    except IntegrityError as e:
        db.rollback()
        error_msg = str(e)
        if "ForeignKeyViolation" in error_msg:
            friendly_msg = "The specified user does not exist. Please create the user first."
        elif "UniqueViolation" in error_msg:
            friendly_msg = "You have already registered this skill."
        elif "CheckViolation" in error_msg:
            print(error_msg)
            friendly_msg = "Check Violation Error"
        else:
            friendly_msg = "A database error occurred while registering the skill."
            
        raise HTTPException(status_code=400, detail=friendly_msg)

def get_skill(db: Session, skip: int = 0, limit: int = 100):
    """
    Retrieve a list of skills from the PostgreSQL database.
    """
    return db.query(models.Skill).offset(skip).limit(limit).all()       

def get_user_by_id(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_user_by_email(db: Session, email: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        logger.warning(f"User requested email lookup for {email}, but it was not found.") # WARN log
        raise HTTPException(status_code=404, detail="User not found")
    return user

def get_all_user_info(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    education = db.query(models.Education).filter(models.Education.user_id == user_id).all()
    experience = db.query(models.Experience).filter(models.Experience.user_id == user_id).all()
    project = db.query(models.Project).filter(models.Project.user_id == user_id).all()
    skill = db.query(models.Skill).filter(models.Skill.user_id == user_id).all()
    return {
        "user": user,
        "education": education,
        "experience": experience,
        "project": project,
        "skill": skill
    }