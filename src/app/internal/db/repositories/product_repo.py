from typing import Optional, List

from app.internal.db.models.products import Product
from app.internal.domain.entities.entities import NotFoundException
from app.internal.domain.entities.product_entities import ProductOut
from app.internal.domain.services.product_service import IProductRepository


class ProductRepository(IProductRepository):
    def get_product_by_id(self, id: int) -> ProductOut:
        product: Optional[Product] = Product.objects.filter(id=id).first()
        if product is None:
            raise NotFoundException(name="Product", id=id)

        return ProductOut.from_orm(product)

    def get_products(self) -> List[ProductOut]:
        return Product.objects.all()
