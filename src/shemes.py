import datetime
from datetime import date
from typing import List
from enums import TypeOfEmployment, Sex, EducationLevels
from pydantic import BaseModel, Field

class VacancyValid(BaseModel):
    position: str
    description: str
    salary: float | None = Field(default=None, gt=0)
    type_of_employment: List[TypeOfEmployment]
    location: str | None = None
    work_experience: int | None = None
    created_at: datetime.datetime = datetime.datetime.now
    updated_at: datetime.datetime = datetime.datetime.now

class CompanyValid(BaseModel):
    name: str
    working_area: List[str]
    description: str
    vacancies: List[VacancyValid]

class ResumeValid(BaseModel):
    position: str
    salary: float = Field(default=None, gt=0)
    name: str
    surname: str
    sex: Sex
    birth_date: date
    email: str | None = Field(default=None, pattern="[A-Za-z0-9]@[a-z].[a-z]")
    phone: str | None = Field(default=None, pattern="+[0-9] ([0-9]) [0-9][0-9][0-9] [0-9][0-9]-[0-9][0-9]")
    city_live: str
    education_level: EducationLevels | None
    institution_name: str
    skills: List[str]
    work_experience: int | None = None
    created_at: datetime.datetime = datetime.datetime.now
    updated_at: datetime.datetime = datetime.datetime.now

class WorkerValid(BaseModel):
    name: str
    surname: str
    age: int = Field(ge=14)
    phone: str | None = Field(default=None, pattern="+[0-9] ([0-9]) [0-9][0-9][0-9] [0-9][0-9]-[0-9][0-9]")
    email: str | None = Field(default=None, pattern="[A-Za-z0-9]@[a-z].[a-z]")
    resumes: List[ResumeValid]

