from sqlalchemy import Integer, String, Column, DateTime, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base

class users(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True),
    usuario = Column(String(255)),
    password = Column(String(255)),
    created_at = Column(DateTime),
    estatus = Column(Boolean, default=False),
    id_persona = Column(Integer)