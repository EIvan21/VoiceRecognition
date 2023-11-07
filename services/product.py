from models.product import Producto as ProductoModel
from schemas.product import Producto

class ProductService():

    def __init__ ( self, db) -> None:

        self.db = db
    
    
    def get_products(self):
        result = self.db.query(ProductoModel).all()
        return result

    def get_product_by_id(self, id):
        result = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()
        return result
    
    def get_product_by_type(self, tipo):
        result = self.db.query(ProductoModel).filter(ProductoModel.tipo == tipo).all()
        return result
    
    def get_product_by_madera(self, madera):
        result = self.db.query(ProductoModel).filter(ProductoModel.madera == madera).all()    
        return result
    
    def get_product_by_type_madera(self, tipo, madera):

        result = self.db.query(ProductoModel).filter(ProductoModel.tipo == tipo).filter(ProductoModel.madera == madera).all()

        return result
    
    def create_product(self, product: Producto):

        new_product = ProductoModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return
    
    def update_producto(self, id: int, data: Producto):
        producto = self.db.query(ProductoModel).filter(ProductoModel.id == id)

        producto_dict = data.dict()
        producto_dict['id'] = id

        producto.update(producto_dict, synchronize_session = False)
        self.db.commit()
        return
    
    def delete_producto(self, id:int):
        producto = self.db.query(ProductoModel).filter(ProductoModel.id == id).first()

        self.db.delete(producto)
        self.db.commit()
        return