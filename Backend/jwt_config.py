from jwt import encode, decode 

def solicita_token(dato:dict)->str:
    token: str=encode(payload=dato, key='mi_clave')