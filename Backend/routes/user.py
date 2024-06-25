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

class model_persona(BaseModel):
    id: str
    nombre: str
    apellido_pat: str
    apellido_mat: str
    created_at: datetime = datetime.now()
    estatus:bool=False

@user.get("/")

def bienvenido():
    return "Bienvenido al sistema de API's"

@user.get("/users")

def get_usuarios():
    return users

@user.post('/users')
def save_usuarios(insert_users:model_user):
    users.append(insert_users)
    #print(insert_users)
    return "Datos guardados"

@user.put('/users/{user_id}')
def update_usuario(user_id: str, updated_user:model_user):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "Datos actualizados"}
        
@user.delete('/users/{user_id}')
def delete_usuario(user_id: str):
    for index, user in enumerate(users):
        if user.id == user_id:
            del users[index]
            return {"message": "Usuario eliminado"}

@persona.get('personas')
@persona.get("/personas")

def get_personas():
    return personas

@persona.post('/personas')
def save_personas(insert_personas:model_persona):
    personas.append(insert_personas)
    #print(insert_users)
    return "Datos guardados"

@persona.put('/personas/{persona_id}')
def update_persona(persona_id: str, updated_persona:model_persona):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = updated_persona
            return {"message": "Datos actualizados"}
        
@persona.delete('/personas/{persona_id}')
def delete_persona(persona_id: str):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return {"message": "Persona eliminado"}
