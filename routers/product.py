from fastapi import APIRouter
from schemas.product import Producto, ProductoCreate
from config.database import Session
from services.product import ProductService
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder

products_router = APIRouter()

@products_router.post("/productos/create/", 
                      tags=["Productos"],
                      status_code=201,
                      summary="Add products here",                               
                      response_model=dict)
async def crear_producto(producto: ProductoCreate):

    db = Session()
    ProductService(db).create_product(producto)
    return JSONResponse(content={"message": "Se ha creado el producto: " + producto.nombre })

@products_router.get('/productos',
                     tags=["Productos"],
                     status_code=200,
                     summary="Todos los productos")
async def obtener_productos():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(content=jsonable_encoder(result))