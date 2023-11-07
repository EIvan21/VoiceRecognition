from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):

    nombre: str = Field(min_length=2, max_length=50)
    ancho: float
    largo: float
    grueso: float
    cantidad: int
    madera: str
    calidad: str
    tipo: str
    costo: float
    precio: float

class ProductoCreate(ProductBase):
    pass

class Producto(ProductBase):
    id: int

    class Config:
        from_attributes =True