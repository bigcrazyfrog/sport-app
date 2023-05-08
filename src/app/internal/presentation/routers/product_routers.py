from typing import List

from ninja import NinjaAPI, Router

from app.internal.domain.entities.entities import NotFoundResponse, ErrorResponse
from app.internal.domain.entities.product_entities import ProductOut
from app.internal.presentation.handlers.product_handlers import ProductHandlers


def get_products_router(product_handlers: ProductHandlers):
    router = Router(tags=['products'])

    router.add_api_operation(
        '',
        ['GET'],
        product_handlers.get_products,
        response={200: List[ProductOut], 400: ErrorResponse},
        description="Get a list of all products",
    )

    router.add_api_operation(
        '/{int:id}',
        ['GET'],
        product_handlers.get_product_by_id,
        response={200: ProductOut, 404: NotFoundResponse},
        description="Get the product by a unique identifier",
    )

    return router


def add_products_router(api: NinjaAPI, product_handlers: ProductHandlers):
    products_handler = get_products_router(product_handlers)
    api.add_router('/products', products_handler)
