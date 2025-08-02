from pydantic import BaseModel
from typing import Optional


class CityBase(BaseModel):
    name: str
    additional_info: str

    class Config:
        # from_attributes = True
        orm_mode = True


class CityCreate(CityBase):
    pass


class City(CityBase):
    id: int


class CityUpdate(CityBase):
    name: Optional[str] = None
    additional_info: Optional[str] = None

    class Config:
        orm_mode = True
