from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    Persona_ID: int
    Nombre_Usuario: str
    Nombre_Usuario: str
    Correo_electronico: str
    Contrasena: str
    Numero_Telefono: str
    Estatus: enumerate
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    ID: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True