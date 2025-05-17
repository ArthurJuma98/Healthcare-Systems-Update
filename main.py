from fastapi import FastAPI

app = FastAPI()


#homepage
@app.get("/")
def index():
    return {"Data": "Welcome to the Homepage"}