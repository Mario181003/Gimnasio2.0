from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class RolBase(BaseModel):
    Nombre: str
    Descripcion: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class UserCreate(RolBase):
    pass

class UserUpdate(RolBase):
    pass

class User(RolBase):
    ID: int
    class Config:
        orm_mode = True
