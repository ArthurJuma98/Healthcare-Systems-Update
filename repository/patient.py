from sqlalchemy.orm import Session
from .. import models

def get_all(db: Session):
    patients = db.query(models.Patient).all()
    return patients