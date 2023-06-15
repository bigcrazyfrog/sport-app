from typing import List, Optional

from app.internal.exceptions.default import NotFoundException
from app.internal.products.db.models import Product
from app.internal.products.domain.entities import ProductOut
from app.internal.products.domain.services import IProductRepository


class ProductRepository(IProductRepository):
    def get_product_by_id(self, id: int) -> ProductOut:
        product: Optional[Product] = Product.objects.filter(id=id).first()
        if product is None:
            raise NotFoundException(name="Product", id=id)

        return ProductOut.from_orm(product)

    def get_products(self) -> List[ProductOut]:
        return Product.objects.all()
