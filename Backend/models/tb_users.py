from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

tb_users = Table("usuarios", meta,
                 Column("id", Integer, primary_key=True),
                 Column("usuario", String(255)),
                 Column("password", String(255)),
                 Column("created_at", datetime = datetime.now()),
                 Column("estatus", bool=False),
                 Column("Id_persona", Integer)
                 )

meta.create_all(engine)