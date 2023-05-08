from typing import List

from app.internal.domain.entities.allergen_entities import AllergenOut


class IAllergenRepository:
    def get_allergen_by_id(self, id: int) -> AllergenOut:
        ...

    def get_allergens(self) -> List[AllergenOut]:
        ...


class AllergenService:
    def __init__(self, allergen_repo: IAllergenRepository):
        self._allergen_repo = allergen_repo

    def get_allergen_by_id(self, id: int) -> AllergenOut:
        return self._allergen_repo.get_allergen_by_id(id=id)

    def get_allergens(self) -> List[AllergenOut]:
        return self._allergen_repo.get_allergens()
