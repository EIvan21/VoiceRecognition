from fastapi import FastAPI
from config.database import Base, engine
from routers.product import products_router
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Creando productos"
app.version = "0.0.1"
app.include_router(products_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las origins
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)


Base.metadata.create_all(bind = engine)

@app.get("/", tags=['home']) #Se agrega el home para agrupar determinadas rutas

def read_root():
    return HTMLResponse('<h1 style=color:red> hola mundo </h1>') #utilizando html