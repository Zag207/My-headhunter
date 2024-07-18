import datetime
from typing import Any, List
from src.enums import WorkLoads
from pydantic import BaseModel, Field, field_validator, field_serializer

from src.schemes.common_types import positiveInt

class VacancyGeneral(BaseModel):
    position: str
    description: str
    salary: float | None = Field(default=None, gt=0)
    workload: List[WorkLoads]
    required_work_experience: int | None = None
    company_id: int = Field(ge=1)
    company_name: str

    @field_validator("workload", mode="before")
    @classmethod
    def transformWorkloads(cls, workloads: Any) -> List[WorkLoads]:
        if type(workloads) is str:
            return list(map(
                lambda workload_str: WorkLoads(workload_str.lower()),
                workloads.split(" ")
            ))
        else:
            return workloads
    
    @field_serializer("workload")
    def transform_field(self, workloads_before: List[WorkLoads]):
        workloads_strs = map(str, workloads_before)
        return " ".join(map(lambda str: str.split(".")[1].lower(), workloads_strs))

class VacancySheme(VacancyGeneral):
    id: positiveInt
    created_at: datetime.datetime
    updated_at: datetime.datetime

class VacancyAdd(VacancyGeneral):
    ...

class VacancyNoID(VacancyGeneral):
    created_at: datetime.datetime
    updated_at: datetime.datetime
    