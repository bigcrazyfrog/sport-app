from typing import List

from ninja.params import Path

from app.internal.allergens.domain.entities import AllergenOut
from app.internal.allergens.domain.services import AllergenService


class AllergenHandlers:
    def __init__(self, allergen_service: AllergenService):
        self._allergen_service = allergen_service

    def get_allergen_by_id(self, request, id: int = Path(...)) -> AllergenOut:
        return self._allergen_service.get_allergen_by_id(id=id)

    def get_allergens(self, request) -> List[AllergenOut]:
        return self._allergen_service.get_allergens()
