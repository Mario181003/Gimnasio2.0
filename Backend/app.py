from fastapi import FastAPI
from routes.user import user
from routes.person import person
# from routes.person import person

app=FastAPI(
    title="Bull´s GYM",
    description="API para el almacenamiento de información de un gimnasio"
)
app.include_router(user)
app.include_router(person)

print ("Hola bienvenido a mi backend")