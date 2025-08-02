import datetime

from pydantic import BaseModel


class TemperatureBase(BaseModel):
    city_id: int
    date_time: datetime.datetime
    temperature: float

    class Config:
        # from_attributes = True
        orm_mode = True


class TemperatureUpdate(TemperatureBase):
    city_id: int
    date_time: datetime.datetime
    temperature: float

    class Config:
        orm_mode = True
