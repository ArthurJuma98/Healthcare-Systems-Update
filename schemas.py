from pydantic import BaseModel
from typing import Optional, List

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    diagnosis: str

    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    patient: List[Patient] = []

    class Config():
        from_attributes = True

class ShowPatient(Patient):
    creator: str | Optional[ShowUser]

    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str