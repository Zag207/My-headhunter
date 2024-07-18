from typing import Annotated
from pydantic import Field

positiveInt = Annotated[int, Field(ge=1)]