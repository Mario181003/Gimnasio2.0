from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import cruds.roles, config.db, schemas.roles, models.roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)
rol = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol.get("/roles/", response_model=List[schemas.roles.Rol], tags=["Roles"])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_users= cruds.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_users

@rol.post("/rol/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def read_user(id: int, db: Session = Depends(get_db)):
    db_user= cruds.roles.get_roles(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol not found")
    return db_user

@rol.post("/rol/", response_model=schemas.roles.Rol, tags=["Roles"])
def create_rol(user: schemas.roles.RolCreate, db: Session = Depends(get_db)):
    db_user = cruds.roles.get_by_rol(db, usuario=rol.Nombre)
    if db_user:
        raise HTTPException(status_code=400, detail="Rol existente intenta nuevamente")
    return cruds.roles.create_roles(db=db, nom=rol)

@rol.put("/user/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def update_user(id: int, user: schemas.roles.RolUpdate, db: Session = Depends(get_db)):
    db_user = cruds.roles.update_roles(db=db, id=id, rol=rol)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no actualizado")
    return db_user

@rol.delete("/user/{id}", response_model=schemas.roles.Rol, tags=["Roles"])
def delete_rol(id: int, db: Session = Depends(get_db)):
    db_user = cruds.roles.delete_roles(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Rol no existe, no se pudo eliminar")
    return db_user