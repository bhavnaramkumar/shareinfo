from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint, CheckConstraint
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    # Changed to String to prevent standard integer max size errors
    phonenumber = Column(String)
    email = Column(String, unique=True, index=True)

# Future tables (like experiences) can be added here
class Education(Base):
    __tablename__ = "education"
    
    __table_args__ = (
        UniqueConstraint('user_id', 'name', 'major', 'minor', name='uq_user_education'),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    major = Column(String(100))
    minor = Column(String(100))
    gpa = Column(Float)

class Experience(Base):
    __tablename__ = "experience"
    
    __table_args__ = (
        UniqueConstraint('user_id', 'work_place', 'job_title', name='uq_user_experience'),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    work_place = Column(String(100))
    location = Column(String(100))
    job_title = Column(String(100))
    start_date = Column(String(100))
    end_date = Column(String(100))
    job_description = Column(String(100))

class Project(Base):
    __tablename__ = "project"
    
    __table_args__ = (
        UniqueConstraint('user_id', 'name', name='uq_user_project'),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(100))
    description = Column(String(100))

class Skill(Base):
    __tablename__ = "skill"
    
    __table_args__ = (
        UniqueConstraint('user_id', 'technical_skills', 'soft_skills', name='uq_user_skill'),
        CheckConstraint('CHAR_LENGTH(technical_skills) >= 3', name='chk_tech_skills_min_len'),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    technical_skills = Column(String(100))
    soft_skills = Column(String(100))