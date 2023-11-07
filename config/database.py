import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# usaremos postgress

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:guitarra2@localhost/productos'

# representa el motor de la base de datos, con el comando “echo=True” para que al momento de realizar la base de datos,
# me muestre por consola lo que esta realizando, que seria el codigo
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Se crea session para conectarse a la base de datos, se enlaza con el comando “bind” y se iguala a engine
Session = sessionmaker(bind = engine)

# Sirve para manipular todas las tablas de la base de datos
Base = declarative_base()