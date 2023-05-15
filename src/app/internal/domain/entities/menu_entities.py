from typing import List

from ninja import Schema
from pydantic import Field

from app.internal.domain.entities.allergen_entities import AllergenOut
from app.internal.domain.entities.product_entities import ProductOut


class MenuOut(Schema):
    id: int
    name: str
    description: str
    allergen: List[AllergenOut]


class MenuContentOut(Schema):
    day: int
    breakfast: List[ProductOut]
    lunch: List[ProductOut]
    dinner: List[ProductOut]
    kalo_sum: int = None


class Filters(Schema):
    allergens: List[int] | None


class RecommendationFilter(Filters):
    kalo: int


class RecommendationOnDay(MenuContentOut):
    snack: List[ProductOut] | None
