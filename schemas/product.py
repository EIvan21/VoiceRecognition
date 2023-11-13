from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):

    nombre: Optional[str] = None
    ancho: Optional[float] = None
    largo: Optional[float] = None
    grueso: Optional[float] = None
    cantidad: Optional[int] = None
    madera: Optional[str] = None
    calidad: Optional[str] = None
    tipo: Optional[str] = None
    costo: Optional[float] = None
    precio: Optional[float] = None

class ProductoCreate(ProductBase):
    pass

class Producto(ProductBase):
   

    class Config:
        from_attributes =True