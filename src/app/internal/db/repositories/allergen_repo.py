from typing import Optional, List

from app.internal.db.models.allergens import Allergen
from app.internal.domain.entities.allergen_entities import AllergenOut
from app.internal.domain.entities.entities import NotFoundException
from app.internal.domain.services.allergen_service import IAllergenRepository


class AllergenRepository(IAllergenRepository):
    def get_allergen_by_id(self, id: int) -> AllergenOut:
        allergen: Optional[Allergen] = Allergen.objects.filter(id=id).first()
        if allergen is None:
            raise NotFoundException(name="Allergen", id=id)

        return AllergenOut.from_orm(allergen)

    def get_allergens(self) -> List[AllergenOut]:
        return Allergen.objects.all()
