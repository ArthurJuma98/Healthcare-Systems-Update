from sqlalchemy import Column, String, Integer, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Patient(Base):
    __tablename__ = "Patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    diagnosis = Column(String)
    user_id = Column(Integer, ForeignKey("Users.id"))

    creator = relationship("User", back_populates="patient_data")

class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    patient_data = relationship("Patient", back_populates="creator")