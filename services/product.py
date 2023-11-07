from models.product import Producto as ProductoModel
from schemas.product import Producto

class ProductService():

    def __init__ ( self, db) -> None:

        self.db = db
    
    def create_product(self, product: Producto):

        new_product = ProductoModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return
    
    def get_products(self):

        result = self.db.query(ProductoModel).all()
        return result
