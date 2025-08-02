
from database import SessionLocal
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from city_crud_api.crud import crud_update_city
from city_crud_api.schemas import CityUpdate
from depedencies import get_db

from temperature_api.crud import get_temperatures_crud, get_temperature_by_city_id_crud
from temperature_api.schemas import TemperatureBase


temperature_router = APIRouter()

@temperature_router.get("/temperatures/", response_model=list[TemperatureBase])
def list_temperatures(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    return get_temperatures_crud(db=db, skip=skip, limit=limit)

@temperature_router.get("/temperatures/{city_id}", response_model=TemperatureBase)
def get_temperature_city_by_id(
    city_id: int,
    db: Session = Depends(get_db)
):
    db_city_temperature = get_temperature_by_city_id_crud(db=db, city_id=city_id)
    if db_city_temperature is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city_temperature


@temperature_router.put("/cities/{city_id}", response_model=TemperatureBase)
def update_city(
        city_id: int,
        city: CityUpdate,
        db: Session = Depends(get_db)
):
    db_city = crud_update_city(db=db, city_id=city_id, city=city)
    if db_city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return db_city

