from pydantic.version import compiled
from pydantic import Field, BaseModel


class Model(BaseModel):
    f = Field(2)


assert compiled
