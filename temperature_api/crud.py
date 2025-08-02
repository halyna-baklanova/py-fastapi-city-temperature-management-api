from sqlalchemy.orm import Session

from models.tempearature_models import Temperature


def get_temperatures_crud(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Temperature).offset(skip).limit(limit).all()

def get_temperature_by_city_id_crud(db: Session, city_id: int):
    return db.query(Temperature).filter(Temperature.city_id == city_id).first()
