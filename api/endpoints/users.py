from ast import Str
from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from sql_app.crud import users as crud
from sql_app.models import users as usermodel
from sql_app.schemas import user as userschema
from sql_app.database import SessionLocal,engine

#from sql_app.database import SessionLocal, engine


usermodel.Base.metadata.create_all(bind=engine)

router = APIRouter()
#app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=userschema.User, tags=['users'])
def create_user(user: userschema.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@router.get("/webhooks", tags=['webhooks'])
def verify_url(hub_mode: str,hub_challenge:int,hub_verify_token: str, db: Session = Depends(get_db)):
   # db_user = crud.get_user_by_email(db, email=user.email)
    #if db_user:
    #    raise HTTPException(status_code=400, detail="Email already registered")
    return hub_challenge#crud.create_user(db=db, user=user)

@router.get("/users/", response_model=List[userschema.User], tags=['users'])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=userschema.User, tags=['users'])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/users/{user_id}/items/", response_model=userschema.Item, tags=['users'])
def create_item_for_user(
    user_id: int, item: userschema.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("/items/", response_model=List[userschema.Item], tags=['users'])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
