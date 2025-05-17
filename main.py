from fastapi import FastAPI
from . import models
from .database import engine
from .router import patient

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(patient.router)