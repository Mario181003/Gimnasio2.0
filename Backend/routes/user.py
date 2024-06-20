from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

user=APIRouter()
users=[]

#Users Model
class model_user(BaseModel):
    id: str
    usuario: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus:bool=False

@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de API's"

@user.get("/users")

def get_usuarios():
    return users

@user.post('/users')

def save_usuarios(users:model_user):
    print(users)
    return "Datos guardados"