from fastapi import FastAPI, APIRouter, Depends, status
from .. import schemas, database
from typing import List
from sqlalchemy.orm import Session
from ..repository import patient

router = APIRouter(
    tags = ["Patients"]
)

get_db = database.get_db

#get all patients
router.get("/all-patients", response_model=List[schemas.ShowPatient])
def all_patients(db: Session=Depends(get_db)):
    return patient.get_all(db)

#create new patient
router.post("create-patient", status_code=status.HTTP_201_CREATED)
def create_patient(request: schemas.Patient, db: Session=Depends(get_db)):
    return patient.create(request, db)

#get patient by id
router.get("get-by-id/{id}", response_model=schemas.ShowPatient, status_code=200)
def get_by_id(id: int, db: Session=Depends(get_db)):
    return patient.patient_id(id, db)

#update patient record
router.put("update-patient/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_patient(id: int, request: schemas.Patient, db: Session=Depends(get_db)):
    return patient.update(id, request, db)

#delete patient record
router.delete("delete-record/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_record(id: int, db: Session=Depends(get_db)):
    return patient.remove(id, db)