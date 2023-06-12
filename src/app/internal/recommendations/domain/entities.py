from typing import List

from ninja import Schema
from pydantic import Field

from app.internal.allergens.domain.entities import AllergenFilters
from app.internal.menus.domain.entities import MenuContentOut
from app.internal.products.domain.entities import ProductOut


class RecommendationFilter(AllergenFilters):
    kalo: int


class RecommendationOnDay(MenuContentOut):
    snack: List[ProductOut] | None
