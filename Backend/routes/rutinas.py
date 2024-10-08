from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import cruds.rutinas, config.db, schemas.rutinas, models.rutinas
from typing import List

key=Fernet.generate_key()
f = Fernet(key)
rutina = APIRouter()

models.rutinas.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rutina.get("/rutinas/", response_model=List[schemas.rutinas.Rutina], tags=["Rutinas"])
def read_rutinas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_rutinas= cruds.rutinas.get_rutinas(db=db, skip=skip, limit=limit)
    return db_rutinas

@rutina.post("/rutina/{id}", response_model=schemas.rutinas.Rutina, tags=["Rutinas"])
def read_rutina(id: int, db: Session = Depends(get_db)):
    db_rutina= cruds.rutinas.get_rutina(db=db, id=id)
    if db_rutina is None:
        raise HTTPException(status_code=404, detail="Rutina not found")
    return db_rutina

@rutina.post("/rutinas/", response_model=schemas.rutinas.Rutina, tags=["Rutinas"])
def create_rutina(rutina: schemas.rutinas.RutinasCreate, db: Session = Depends(get_db)):
    db_rutina = cruds.rutinas.get_rutina_by_nombre(db, rutina=rutina.Nombre)
    if db_rutina:
        raise HTTPException(status_code=400, detail="Rutina existente intenta nuevamente")
    return cruds.rutinas.create_rutina(db=db, rutina=rutina)

@rutina.put("/rutina/{id}", response_model=schemas.rutinas.Rutina, tags=["Rutinas"])
def update_rutina(id: int, rutina: schemas.rutinas.RutinasUpdate, db: Session = Depends(get_db)):
    db_rutina = cruds.rutinas.update_rutina(db=db, id=id, rutina=rutina)
    if db_rutina is None:
        raise HTTPException(status_code=404, detail="Rutina no existe, no actualizado")
    return db_rutina

@rutina.delete("/rutina/{id}", response_model=schemas.rutinas.Rutina, tags=["Rutinas"])
def delete_rutina(id: int, db: Session = Depends(get_db)):
    db_rutina = cruds.rutinas.delete_rutina(db=db, id=id)
    if db_rutina is None:
        raise HTTPException(status_code=404, detail="Rutina no existe, no se pudo eliminar")
    return db_rutina
