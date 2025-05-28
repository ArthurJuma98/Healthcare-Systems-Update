from fastapi import FastAPI
from . import models
from .database import engine
from .router import patient, user

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(patient.router)
app.include_router(user.router)