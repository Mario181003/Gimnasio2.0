from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

persona=APIRouter()
personas=[]

class model_persona(BaseModel):
    id: str
    nombre: str
    apellido_pat: str
    apellido_mat: str
    direccion: str
    telefono: str
    correo: str
    sangre: str
    created_at: datetime = datetime.now()
    estatus:bool=False

@persona.get('/personas', tags=["Personas"])

def get_personas():
    return personas

@persona.post('/personas', tags=["Personas"])
def save_personas(insert_personas:model_persona):
    personas.append(insert_personas)
    #print(insert_users)
    return "Datos guardados"

@persona.put('/personas/{persona_id}', tags=["Personas"])
def update_persona(persona_id: str, updated_persona:model_persona):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = updated_persona
            return {"message": "Datos actualizados"}
        
@persona.delete('/personas/{persona_id}', tags=["Personas"])
def delete_persona(persona_id: str):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return {"message": "Persona eliminado"}
