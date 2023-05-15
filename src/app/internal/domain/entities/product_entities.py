from ninja import Schema
from pydantic import Field

from app.internal.domain.entities.allergen_entities import AllergenOut


class ProductOut(Schema):
    id: int
    name: str
    kilocalories: int
    proteins: float
    fats: float
    carb: float
    allergens: list[AllergenOut] = None
    proportion: float
