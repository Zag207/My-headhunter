from fastapi import APIRouter, Path
from typing import List, Annotated, Union

from sqlalchemy import select, delete, update


from src.schemes.vacancy_shemes import *
from src.db_core import async_session_factory
from src.models import VacancyOrm, CompanyOrm

router = APIRouter(
    prefix="/vacancy",
    tags=["Vacancy"]
)

@router.post("/")
async def create_vacancy(vacancy: VacancyAdd):
    existing_company_q = select(CompanyOrm).filter_by(id=vacancy.company_id)

    async with async_session_factory() as session:
        check_res = await session.execute(existing_company_q)
        checking_company = check_res.scalars().first()

        if checking_company is None:
            return
        else:
            vacancy_dict = vacancy.model_dump()
            print(vacancy_dict)

            vacancy_orm = VacancyOrm(**vacancy_dict)
            session.add(vacancy_orm)
            await session.commit()
            pass

@router.get("/", response_model=List[VacancySheme])
async def get_all_vacancies() -> List[VacancySheme]:
    query = select(VacancyOrm)

    async with async_session_factory() as session:
        res = await session.execute(query)
    
    companies = res.scalars().all()

    return [VacancySheme.model_validate(row, from_attributes=True) for row in companies]

@router.get("/{vacancy_id}", response_model=Union[VacancySheme, None])
async def get_vacancy_by_id(vacancy_id: Annotated[int, Path(ge=1)]):
    query = select(VacancyOrm).filter_by(id=vacancy_id)

    async with async_session_factory() as session:
        res = await session.execute(query)
    
    vacancy = res.scalars().first()
    
    if vacancy is None:
        return None
    else:
        return VacancySheme.model_validate(vacancy, from_attributes=True)

@router.delete("/{vacancy_id}", response_model=Union[VacancySheme, None])
async def delete_vacancy(vacancy_id: Annotated[int, Path(ge=1)]):
    async with async_session_factory() as session:
        get_vacancy_query = select(VacancyOrm).filter_by(id=vacancy_id)
        res = await session.execute(get_vacancy_query)
        vacancy = res.scalars().first()

        if vacancy is not None:
            delete_vacancy_query = delete(VacancyOrm).filter_by(id=vacancy_id)
            await session.execute(delete_vacancy_query)
            await session.commit()
    
    if vacancy is not None:
        return VacancySheme.model_validate(vacancy, from_attributes=True)
    else:
        return None

@router.put("/{vacancy_id}")
async def change_company_data(vacancy_id: Annotated[int, Path(ge=1)], vac: VacancyAdd) -> None:
    q = update(VacancyOrm).values(**vac.model_dump()).filter_by(id=vacancy_id)

    async with async_session_factory() as session:
        await session.execute(q)
        await session.commit()
