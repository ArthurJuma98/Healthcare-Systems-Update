from fastapi import HTTPException, status
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

def patient_id(id: int, db: Session):
    patient = db.query(models.Patient).filter(models.Patient.id == id).first()

    if not patient:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Patient with the id: {id} not found!")
    return patient

def update(id: int, request: schemas.Patient, db: Session):
    patient_query = db.query(models.Patient).filter(models.Patient.id == id)
    patient = patient_query.first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Patient with ID {id} not found."
        )
    
    patient_query.update(request.model_dump(), synchronize_session=False)
    db.commit()

    return {"message": "Patient record updated successfully"}