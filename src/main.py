from fastapi import FastAPI

from src.routers.company_router import router as company_router
from src.routers.vacancy_router import router as vacancy_router

app = FastAPI(title="MyHH")

app.include_router(company_router)
app.include_router(vacancy_router)
