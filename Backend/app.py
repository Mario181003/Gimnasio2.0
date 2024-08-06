from fastapi import FastAPI
from routes.user import user
from routes.person import person
from routes.roles import rol
from routes.usuarios_roles import userrol
from routes.rutinas import rutina
from routes.ejercicios_rutinas import ejcrtn
from routes.progra_salud import progra_salud

app=FastAPI(
    title="Bull´s GYM",
    description="API para el almacenamiento de información de un gimnasio"
)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(rutina)
app.include_router(ejcrtn)
app.include_router(progra_salud)

print ("Hola bienvenido a mi backend")
