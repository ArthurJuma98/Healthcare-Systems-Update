from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    diagnosis: str

class User(BaseModel):
    name: str
    email: str
    password: str
