from fastapi import FastAPI, APIRouter, Depends
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
router.post("create-patient")
def create_patient(request: schemas.Patient, db: Session=Depends(get_db)):
    return patient.create(request, db)