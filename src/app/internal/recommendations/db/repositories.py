from typing import Optional, List

from app.internal.allergens.domain.entities import AllergenFilters
from app.internal.menus.db.models import Menu
from app.internal.menus.domain.entities import MenuOut
from app.internal.products.db.models import Product
from app.internal.products.domain.entities import ProductOut
from app.internal.recommendations.db.models import Recommendation
from app.internal.recommendations.domain.entities import RecommendationOnDay, RecommendationFilter
from app.internal.recommendations.domain.services import IRecommendationRepository


class RecommendationRepository(IRecommendationRepository):
    def _get_menu_model(self, allergen_list: List[int]) -> Menu:
        if allergen_list is None:
            menu: Optional[Menu] = Menu.objects.filter(allergen=None).order_by("?").first()
        else:
            menu: Optional[Menu] = Menu.objects.filter(allergen__id__in=allergen_list).order_by("?").first()

        if menu is None:
            menu: Optional[Menu] = Menu.objects.all().order_by("?").first()

        return menu

    def get_recommendation_by_menu(self, allergens: AllergenFilters) -> MenuOut:
        menu = self._get_menu_model(allergen_list=allergens.allergens)

        return MenuOut.from_orm(menu)

    def _fill_snack(self, rec: RecommendationOnDay, rec_filter: RecommendationFilter, difference: int = None):
        rec.snack = []
        if difference is None:
            difference = rec_filter.kalo

        while difference - rec.kalo_sum > 50:
            if rec_filter.allergens is None:
                product = Product.objects.filter(kilocalories__lt=70).order_by("?").first()
            else:
                product = Product.objects.filter(kilocalories__lt=70) \
                    .exclude(allergens__id__in=rec_filter.allergens).order_by("?").first()

            rec.kalo_sum += product.kilocalories * product.proportion
            rec.snack.append(ProductOut.from_orm(product))

    def get_recommendation_on_day(self, rec_filter: RecommendationFilter) -> RecommendationOnDay:
        menu = self._get_menu_model(allergen_list=rec_filter.allergens)
        recommendation = Recommendation.objects.filter(menu=menu).order_by("?").first()

        rec = RecommendationOnDay.from_orm(recommendation)
        self._fill_snack(rec=rec, rec_filter=rec_filter)

        return rec

    def get_recommendation_on_week(self, rec_filter: RecommendationFilter) -> List[RecommendationOnDay]:
        menu = self._get_menu_model(allergen_list=rec_filter.allergens)
        recommendations = Recommendation.objects.filter(menu=menu).order_by("day")

        recs = []
        difference = rec_filter.kalo
        for recommendation in recommendations:
            rec = RecommendationOnDay.from_orm(recommendation)

            self._fill_snack(rec=rec, rec_filter=rec_filter, difference=difference)
            difference += rec_filter.kalo - rec.kalo_sum
            recs.append(rec)

        return recs
