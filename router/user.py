from fastapi import APIRouter, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    tags=["Users"]
)

get_db = database.get_db

#create a new user
router.post("/create-user", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request, db)

#get user by id
router.get("/user-by-id/{id}", response_model=schemas.ShowUser)
def user_by_id(id: int, db: Session=Depends(get_db)):
    return user.get_user(id, db)