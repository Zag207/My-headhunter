from typing import List
from pydantic import BaseModel, Field
from src.schemes.vacancy_shemes import VacancySheme
from src.schemes.common_types import positiveInt


class CompanySheme(BaseModel):
    id: positiveInt
    name: str
    description: str

    vacancies: List[VacancySheme] | None = Field(default=None)


class CompanyNoID(BaseModel):
    name: str
    description: str