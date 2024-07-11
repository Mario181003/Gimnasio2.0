import models.usuarios_roles
import schemas.usuarios_roles
from sqlalchemy.orm import Session
import models, schemas

# Funcion Correcta
def get_usuario_rol(db: Session, id: int):
    return db.query(models.usuarios_roles.Usuario_Rol).filter(models.usuarios_roles.Usuario_Rol.ID == id).first()

def get_user_by_usuario(db: Session, usuario: str):
    return db.query(models.users.User).filter(models.users.User.Nombre_Usuario == usuario).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.users.User).offset(skip).limit(limit).all()

# Funcion correcta
def create_usuario_rol(db: Session, usuario_rol: schemas.usuarios_roles.UsuarioRolCreate):
    db_usuario_rol = models.usuarios_roles.Usuario_Rol(Usuario_ID=usuario_rol.Usuario_ID, 
                                                       Rol_ID=usuario_rol.Rol_ID, 
                                                       Estatus=usuario_rol.Estatus, 
                                                    Fecha_Registro=usuario_rol.Fecha_Registro, 
                                                    Fecha_Actualizacion=usuario_rol.Fecha_Actualizacion
                                )
    db.add(db_usuario_rol)
    db.commit()
    db.refresh(db_usuario_rol)
    return db_usuario_rol

def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.ID == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user