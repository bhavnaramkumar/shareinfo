from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    phonenumber: str
    email: str

class UserResponse(UserCreate):
    class Config:
        from_attributes = True

class UserAllInfoResponse(BaseModel):
    user: UserResponse
    education: list['EducationResponse'] = []
    experience: list['ExperienceResponse'] = []
    project: list['ProjectResponse'] = []
    skill: list['SkillResponse'] = []
    class Config:
        from_attributes = True

class EducationCreate(BaseModel):
    user_id: int
    name: str
    major: str
    minor: str
    gpa: float

class EducationResponse(EducationCreate):
    class Config:
        from_attributes = True

class ExperienceCreate(BaseModel):
    user_id: int
    work_place: str
    location: str
    job_title: str
    start_date: str
    end_date: str
    job_description: str

class ExperienceResponse(ExperienceCreate):
    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    user_id: int
    name: str
    description: str

class ProjectResponse(ProjectCreate):
    class Config:
        from_attributes = True

class SkillCreate(BaseModel):
    user_id: int
    technical_skills: str = Field(min_length=3)
    soft_skills: str

class SkillResponse(SkillCreate):
    class Config:
        from_attributes = True