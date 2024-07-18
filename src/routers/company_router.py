from fastapi import APIRouter, Path

from typing import List, Annotated, Optional

from sqlalchemy import select, update, delete
from sqlalchemy.orm import selectinload


from src.db_core import async_session_factory
from src.models import CompanyOrm
from src.schemes.company_shemes import CompanySheme, CompanyNoID

router = APIRouter(
    prefix="/company",
    tags=["Company"]
)

@router.get("/{company_id}")
async def get_company_by_id(company_id: int):
    q = select(CompanyOrm).filter_by(id=company_id).options(selectinload(CompanyOrm.vacancies))

    async with async_session_factory() as session:
        res = await session.execute(q)
    
    company = res.scalars().first()
    
    return CompanySheme.model_validate(company, from_attributes=True)

@router.get("/", response_model=List[CompanySheme])
async def get_all_companies() -> List[CompanySheme]:
    q = select(CompanyOrm).options(selectinload(CompanyOrm.vacancies))

    async with async_session_factory() as session:
        res = await session.execute(q)
    
    companies = res.scalars().all()
    return [CompanySheme.model_validate(company, from_attributes=True) for company in companies]

@router.get("/{company_name}", response_model=List[CompanySheme])
async def get_companies_by_name(company_name: str) -> List[CompanySheme]:
    q = select(CompanyOrm).filter_by(name=company_name).options(selectinload(CompanyOrm.vacancies))

    async with async_session_factory() as session:
        res = await session.execute(q)
    
    companies = res.scalars().all()
    return [CompanySheme.model_validate(company, from_attributes=True) for company in companies]


@router.put("/{company_id}")
async def change_company_data(company_id: Annotated[int, Path(ge=1)], comp: CompanyNoID) -> None:
    q = update(CompanyOrm).values(**comp.model_dump()).filter_by(id=company_id)

    async with async_session_factory() as session:
        await session.execute(q)
        await session.commit()

@router.post("/", response_model=CompanyNoID)
async def create_company(company: CompanyNoID) -> CompanyNoID:
    company_orm = CompanyOrm(**company.model_dump())

    async with async_session_factory() as session:
        session.add(company_orm)
        await session.commit()

    return company.model_dump()

# TODO: если запись не найдена, то пусть возвращает ошибку
@router.delete("/{company_id}", response_model=Optional[CompanySheme])
async def delete_company(company_id: Annotated[int, Path(ge=1)]) -> CompanySheme | None:
    async with async_session_factory() as session:
        get_company_query = select(CompanyOrm).filter_by(id=company_id).options(selectinload(CompanyOrm.vacancies))
        res = await session.execute(get_company_query)
        company = res.scalars().first()

        if company is not None:
            delete_company_query = delete(CompanyOrm).filter_by(id=company_id)
            await session.execute(delete_company_query)
            await session.commit()
    
    if company is not None:
        return CompanySheme.model_validate(company, from_attributes=True)
    else:
        return None
    