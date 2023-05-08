from ninja import Schema

from app.internal.domain.entities.product_entities import ProductOut


class RecommendationOut(Schema):
    day: int
    breakfast: ProductOut
    lunch: ProductOut
    dinner: ProductOut
