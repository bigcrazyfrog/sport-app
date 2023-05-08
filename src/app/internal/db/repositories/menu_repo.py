from typing import Optional

#
# class MenuRepository(IMenuRepository):
#     def __init__(self):
#         self._tables = {
#             ""
#         }
#
#     def get_allergen_by_id(self, id: int) -> AllergenOut:
#         allergen: Optional[Allergen] = Allergen.objects.filter(id=id).first()
#         if allergen is None:
#             raise NotFoundException(name="Allergen", id=id)
#
#         return AllergenOut.from_orm(allergen)
#
#     def get_allergens(self) -> List[AllergenOut]:
#         return Allergen.objects.all()
