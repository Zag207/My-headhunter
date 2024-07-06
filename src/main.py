from fastapi import FastAPI

app = FastAPI(
    title="MyHH",
)

@app.get("/company/{company_id}")
async def get_company_info(company_id: int):
    ...

@app.post("/company")
async def create_company():
    ...

# Create endpoints for vacancies, resumes, users
