from typing import List

from app.internal.products.domain.entities import ProductOut


class IProductRepository:
    def get_product_by_id(self, id: int) -> ProductOut:
        ...

    def get_products(self) -> List[ProductOut]:
        ...


class ProductService:
    def __init__(self, product_repo: IProductRepository):
        self._product_repo = product_repo

    def get_product_by_id(self, id: int) -> ProductOut:
        return self._product_repo.get_product_by_id(id=id)

    def get_products(self) -> List[ProductOut]:
        return self._product_repo.get_products()
