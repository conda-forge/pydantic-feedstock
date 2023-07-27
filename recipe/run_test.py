from pydantic import Field, BaseModel


class Model(BaseModel):
    f = Field(2)
