from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.rol import rol
# from routes.person import person

app=FastAPI(
    title="Bull´s GYM",
    description="API para el almacenamiento de información de un gimnasio"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)

print ("Hola bienvenido a mi backend")