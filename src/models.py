from sqlalchemy import func, ForeignKey
from src.db_core import Base
from typing import Annotated, List
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship

intpk = Annotated[int, mapped_column(primary_key=True)]

class VacancyOrm(Base):
    __tablename__ = 'vacancies'

    id: Mapped[intpk]
    position: Mapped[str]
    description: Mapped[str]
    salary: Mapped[int | None]
    workload: Mapped[str]
    required_work_experience: Mapped[int | None]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    company_id: Mapped[int] = mapped_column(ForeignKey('companies.id', ondelete='CASCADE'), nullable=False)
    company_name: Mapped[str]

    company: Mapped["CompanyOrm"] = relationship(
        back_populates="vacancies",
    )

class CompanyOrm(Base):
    __tablename__ = 'companies'

    id: Mapped[intpk]
    name: Mapped[str]
    description: Mapped[str]

    vacancies: Mapped[List["VacancyOrm"]] = relationship(
        back_populates="company"
    )

class ResumeOrm(Base):
    __tablename__ = 'resumes'

    id: Mapped[intpk]
    position: Mapped[str]
    salary: Mapped[int | None] = mapped_column(default=None)
    sex: Mapped[str]
    birth_date: Mapped[datetime.datetime]
    email: Mapped[str | None]
    phone: Mapped[str | None]
    education_level: Mapped[str | None]
    skills: Mapped[str]
    work_experience: Mapped[int | None] = mapped_column(default=None)
    worker_id: Mapped[int] = mapped_column(ForeignKey('workers.id'), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    worker: Mapped["WorkerOrm"] = relationship(
        back_populates="resumes",
    )

class WorkerOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    name: Mapped[str]
    surname: Mapped[str]
    sex: Mapped[str]
    age: Mapped[int]
    phone_number: Mapped[str | None] = mapped_column(default=None, )
    email: Mapped[str | None] = mapped_column(default=None)

    resumes: Mapped[List["ResumeOrm"]] = relationship(
        back_populates="worker"
    )
