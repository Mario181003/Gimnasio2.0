from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import cruds.usuarios_roles, config.db, schemas.usuarios_roles, models.usuarios_roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)
usuario_rol = APIRouter()

models.usuarios_roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario_rol.get("/usuarios_roles/", response_model=List[schemas.usuarios_roles.UsuarioRol], tags=["Usuarios Roles"])
def read_usuario_rol(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_useriosRol= cruds.usuarios_roles.get_usuario_rol(db=db, skip=skip, limit=limit)
    return db_useriosRol

# @usuario_rol.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
# def read_user(id: int, db: Session = Depends(get_db)):
#     db_user= cruds.users.get_user(db=db, id=id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

@usuario_rol.post("/usuarios_roles/", response_model=schemas.usuarios_roles.UsuarioRolCreate, tags=["Usuarios Roles"])
def create_user(user: schemas.usuarios_roles.UsuarioRolCreate, db: Session = Depends(get_db)):
    db_user = cruds.usuarios_roles.create_usuario_rol(db, usuario_rol=user.Nombre_Usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return cruds.usuarios_roles.create_usuario_rol(db=db, user=user)

# @user.put("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
# def update_user(id: int, user: schemas.users.UserUpdate, db: Session = Depends(get_db)):
#     db_user = cruds.users.update_user(db=db, id=id, user=user)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
#     return db_user

# @user.delete("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
# def delete_user(id: int, db: Session = Depends(get_db)):
#     db_user = cruds.users.delete_user(db=db, id=id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
#     return db_user