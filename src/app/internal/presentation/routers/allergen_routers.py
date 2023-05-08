from typing import List

from ninja import NinjaAPI, Router

from app.internal.domain.entities.allergen_entities import AllergenOut
from app.internal.domain.entities.entities import NotFoundResponse, ErrorResponse
from app.internal.presentation.handlers.allergen_handlers import AllergenHandlers


def get_allergens_router(allergen_handlers: AllergenHandlers):
    router = Router(tags=['allergens'])

    router.add_api_operation(
        '',
        ['GET'],
        allergen_handlers.get_allergens,
        response={200: List[AllergenOut], 400: ErrorResponse},
        description="Get a list of all allergens",
    )

    router.add_api_operation(
        '/{int:id}',
        ['GET'],
        allergen_handlers.get_allergen_by_id,
        response={200: AllergenOut, 404: NotFoundResponse},
        description="Get the allergen by a unique identifier",
    )

    return router


def add_allergens_router(api: NinjaAPI, allergen_handlers: AllergenHandlers):
    allergens_handler = get_allergens_router(allergen_handlers)
    api.add_router('/allergens', allergens_handler)
