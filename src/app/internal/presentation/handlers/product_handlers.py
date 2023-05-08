from typing import List

from ninja.params import Path

from app.internal.domain.entities.product_entities import ProductOut
from app.internal.domain.services.product_service import ProductService


class ProductHandlers:
    def __init__(self, product_service: ProductService):
        self._product_service = product_service

    def get_product_by_id(self, request, id: int = Path(...)) -> ProductOut:
        return self._product_service.get_product_by_id(id=id)

    def get_products(self, request) -> List[ProductOut]:
        return self._product_service.get_products()
