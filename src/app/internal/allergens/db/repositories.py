from typing import Optional, List

from app.internal.allergens.db.models import Allergen
from app.internal.allergens.domain.entities import AllergenOut
from app.internal.allergens.domain.services import IAllergenRepository
from app.internal.exceptions.default import NotFoundException


class AllergenRepository(IAllergenRepository):
    def get_allergen_by_id(self, id: int) -> AllergenOut:
        allergen: Optional[Allergen] = Allergen.objects.filter(id=id).first()
        if allergen is None:
            raise NotFoundException(name="Allergen", id=id)

        return AllergenOut.from_orm(allergen)

    def get_allergens(self) -> List[AllergenOut]:
        return Allergen.objects.all()
