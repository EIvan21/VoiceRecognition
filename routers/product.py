from fastapi import APIRouter
from schemas.product import Producto, ProductoCreate
from config.database import Session
from services.product import ProductService
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import  HTTPException, status, Path, Query, Depends

products_router = APIRouter()


#-------------------GETTING ALL PRODUCTS -----------------------------

@products_router.get('/productos',
                     tags=["Productos"],
                     status_code=200,
                     summary="Todos los productos")
async def obtener_productos():
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(content=jsonable_encoder(result))

#---------------GETING PRODUCT BY ID ----------------------------------

@products_router.get(path='/productos/read/{id}',
                     tags=["Productos"],
                     status_code=status.HTTP_200_OK,
                     summary="Product by id"                     
                     )
async def get_movie_by_id(id:int = Path(ge=0, le=2000)):
    
    """
    Obtener el producto por id por parametro de ruta
    """

    db = Session()
    result = ProductService(db).get_product_by_id(id)

    if not result:
        raise HTTPException(status_code=404, detail="Id product not found")

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#------------------- GETTING PRODUCT BY TYPE or MADERA ----------------------

@products_router.get(path="/productos/read/",
                     tags=["Productos"],
                     status_code=status.HTTP_200_OK,
                     summary="Producto por tipo o madera"
                     )
async def get_product_by_type_or_madera(tipo: str = Query(min_length=1, max_length=15, default=None), madera:str = Query(default=None)):


    """Obtener productos por el tipo de material (Tabla, Tablero, Construcción)"""

    db = Session()

    if tipo is None and madera is None:
        raise HTTPException(status_code=404, detail="Escribe algun tipo o madera del producto")
    
    elif tipo is None:
        result = ProductService(db).get_product_by_madera(madera)
        if not result:
            raise HTTPException(status_code=404, detail="Madera no encontrada")
        
    
    elif madera is None:
        result = ProductService(db).get_product_by_type(tipo)
        if not result:
            raise HTTPException(status_code=404, detail="Tipo de producto no encontrado")
    else:

        result = ProductService(db).get_product_by_type_madera(tipo,madera)
        if not result:
            raise HTTPException(status_code=404, detail="Tipo de producto no encontrado")
        
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

#------------------CREATING A NEW PRODUCT ------------------

@products_router.post("/productos/create/", 
                      tags=["Productos"],
                      status_code=201,
                      summary="Add products here",                               
                      response_model=dict)
async def crear_producto(producto: ProductoCreate):

    db = Session()
    ProductService(db).create_product(producto)
    return JSONResponse(content={"message": "Se ha creado el producto: " + producto.nombre })

#---------------- UPDATING AN EXISTING PRODUCT ------------------------------
@products_router.put(path='/products/update/{id}',
                     tags=["Productos"],
                     status_code=status.HTTP_200_OK,
                     summary="Update product"                    
                     )
async def update_product(id: int, product: Producto):
    """Actualizar el producto por parámetros en el body buscando por ID"""

    db = Session()
    result = ProductService(db).get_product_by_id(id)
    actual_name = result.nombre

    if not result:
        raise HTTPException(status_code=404, detail="Producto no encontrado, no se actualizó")
    else:

        ProductService(db).update_producto(id, product)
        
        return JSONResponse(status_code=200, content = {"message": "Se ha modificado el producto " + actual_name})


#------------ DELETING PRODUCT -----------------------------------------------------

@products_router.delete(path='/delete/{id}',
                        tags=["Productos"],
                        status_code=status.HTTP_200_OK,
                        summary="Delete product"
                        
                        )
async def delete_product(id: int):

    """ Eliminar pelicula por id """

    db = Session()
    result = ProductService(db).get_product_by_id(id)

    if not result:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    else:
        ProductService(db).delete_producto(id)