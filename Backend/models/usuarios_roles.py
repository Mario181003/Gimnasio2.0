from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base
import models.roles
import models.users

class Usuario_Rol(Base):
    __tablename__ = "tbd_usuarios_roles"

    ID = Column(Integer, primary_key=True, index=True)
    Usuario_ID = Column(Integer, ForeignKey('tbb_usuarios.ID'))
    Rol_ID = Column(Integer, ForeignKey('tbc_roles.ID'))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
    #items = relationship("Item", back_populates="owner") Clave Foranea