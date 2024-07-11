from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class UsuarioRolBase(BaseModel):
    Usuario_ID: int
    Rol_ID: int
    Estatus: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(UsuarioRolBase):
    pass

class UserUpdate(UsuarioRolBase):
    pass

class UsuarioRolBase(UsuarioRolBase):
    ID: int
    Persona_ID: int
    Rol_ID: int
    class Config:
        orm_mode = True
