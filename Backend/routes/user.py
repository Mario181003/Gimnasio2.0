from fastapi import APIRouter, HTTPExeption, Depends
from sqlalchemy.orm import Session
from crytography.fernet import Fernet
from crud.users, config.db, schemas.users, mnodels.users
import routes.user
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

user = APIRouter()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/users", response_model=list[schemas.users.User],tags=["Usuarios"] )
def read_users(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud_get_users(db, skip=skip, limit=limit)
    return users

@user.post("/users/{id}", response_model=schemas.users.User, tags=["Usuarios"] )
def read_user(skip: int=0, db: Session=Depends(get_db)):
    db_users = crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPExeotion(status_code=404, detail="User not found")
    return db_users

@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"] )
def create_user(user: schemas.users.UserCreate, db: Session=Depends(get_db)):
    db_users = crud.users.get_user_by_usuario(db, usuario=user.usuario)
    if db_user:
        raise HTTPExeotion(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

@user.put("/users/{user_id}", response_model=schemas.users.User, tags=["Usuarios"])
def update_user(id: int, user: schemas.users.UserUpdate, db: Session=Depends(get_db)):
    db_user = crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPExeotion(status_code=404, detail="Usuario no existe, no actualizado")
    return db_users

@user.delete("/users/{user_id}", response_model=schemas.users.User, tags=["Usuarios"])
def dlete_user(id: int, db: Session=Depends(get_db)):
    db_user = crud.users.delet_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se puede eliminar")
    return db_user