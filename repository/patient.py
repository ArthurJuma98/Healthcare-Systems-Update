from sqlalchemy.orm import Session
from .. import models, schemas

def get_all(db: Session):
    patients = db.query(models.Patient).all()
    return patients

def create(db: Session, request: schemas.Patient):
    new_patient = models.Patient(name=request.name, age=request.age, gender=request.gender, diagnosis=request.diagnosis)

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient