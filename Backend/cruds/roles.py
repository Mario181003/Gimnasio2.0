import models.roles
import schemas.roles
from sqlalchemy.orm import Session
import models
import schemas

def get_rol(db: Session, id: int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()

def get_user_by_rol(db: Session, usuario: str):
    return db.query(models.roles.Rol).filter(models.roles.Rol.Nombre == usuario).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: schemas.roles.RolCreate):
    db_user = models.roles.Rol(Nombre = rol.Nombre, Descripcion = rol.Descripcion, Estatus = rol.Estatus, Fecha_Registro = rol.Fecha_Registro, Fecha_Actualizacion = rol.Fecha_Actualizacion)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_rol(db: Session, id: int, user: schemas.roles.RolUpdate):
    db_user = db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_person(db: Session, id: int):
    db_person = db.query(models.roles.Rol).filter(models.roles.Rol.ID == id).first()
    if db_person:
        db.delete(db_person)
        db.commit()
    return db_person