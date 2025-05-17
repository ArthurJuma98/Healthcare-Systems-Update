from sqlalchemy import Column, String, Integer, ForeignKey
from .database import Base


class Patient(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    diagnosis = Column(String)