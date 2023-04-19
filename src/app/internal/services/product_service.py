from app.internal.models.products import Product


class ProductService:
    @staticmethod
    def get_all():
        products = Product.objects.all()

        res = dict()
        for product in products:
            res[product.id] = {
                "name": product.name,
                "kilocalories": product.kilocalories,
                "proteins": product.proteins,
                "fats": product.fats,
                "carb": product.carb,
            }

        return res

    @staticmethod
    def get_by_id(id: int):
        product = Product.objects.filter(id=id) \
            .values("id", "name", "kilocalories", "proteins", "fats", "carb").first()

        if product is None:
            return {"id": id, "exist": False}

        product["exist"] = True
        return product

    @staticmethod
    def get_rand():
        return Product.objects.order_by('?')\
            .values("id", "name", "kilocalories", "proteins", "fats", "carb").first()
