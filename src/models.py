from src.database.db_config import Base
from enums import TypeOfEmployment, Sex, EducationLevels
from typing import List
from sqlalchemy.orm import Mapped, mapped_column


class VacancyOrm(Base):
    __tablename__ = 'vacancies'

    vacancy_id: Mapped[int] = mapped_column(primary_key=True, auto_increment=True)
    position: Mapped[str] = mapped_column()
    description: Mapped[str]
    salary: Mapped[str | None]
    type_of_employment: Mapped[List[TypeOfEmployment]]
    location: Mapped[str | None]
    work_experience: Mapped[int | None]

class CompanyValid(Base):
    name: str
    working_area: List[str]
    description: str
    vacancies: List[VacancyValid]

class ResumeValid(Base):
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

class WorkerValid(Base):
    name: str
    surname: str
    age: int = Field(ge=14)
    phone: str | None = Field(default=None, pattern="+[0-9] ([0-9]) [0-9][0-9][0-9] [0-9][0-9]-[0-9][0-9]")
    email: str | None = Field(default=None, pattern="[A-Za-z0-9]@[a-z].[a-z]")
    resumes: List[ResumeValid]