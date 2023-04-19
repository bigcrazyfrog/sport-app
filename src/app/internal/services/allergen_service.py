from app.internal.models.allergens import Allergen


class AllergenService:
    @staticmethod
    def get_all() -> dict:
        allergens = Allergen.objects.all()

        res = dict()
        for i in allergens:
            res[i.id] = {"name": i.name}

        return res

    @staticmethod
    def get_by_id(id: int):
        allergen = Allergen.objects.filter(id=id) \
            .values("id", "name").first()

        if allergen is None:
            return {"id": id, "exist": False}

        allergen["exist"] = True
        return allergen
