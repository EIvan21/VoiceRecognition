from config.database import Base
from sqlalchemy import Column, Integer, String, Numeric


class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    ancho = Column(Numeric)
    largo = Column(Numeric)
    grueso = Column(Numeric)
    cantidad = Column(Integer)
    madera = Column(String)
    calidad = Column(String)
    tipo = Column(String)
    costo = Column(Numeric)
    precio = Column(Numeric)
