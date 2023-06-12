from typing import List

from ninja import Schema
from pydantic import Field

from app.internal.allergens.domain.entities import AllergenOut
from app.internal.products.domain.entities import ProductOut


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
