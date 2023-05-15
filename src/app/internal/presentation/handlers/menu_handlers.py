from typing import List

from ninja.params import Path
from ninja import Query

from app.internal.domain.entities.menu_entities import MenuOut, MenuContentOut, Filters, RecommendationFilter, \
    RecommendationOnDay
from app.internal.domain.services.menu_services import MenuService
from app.internal.domain.services.recomendation_services import RecommendationService


class MenuHandlers:
    def __init__(self, menu_service: MenuService, recommendation_service: RecommendationService):
        self._menu_service = menu_service
        self._recommendation_service = recommendation_service

    def get_menu_by_id(self, request, id: int = Path(...)) -> MenuOut:
        return self._menu_service.get_menu_by_id(id=id)

    def get_menu_list(self, request) -> List[MenuOut]:
        return self._menu_service.get_menu_list()

    def get_menu_content(self, request, id: int) -> List[MenuContentOut]:
        return self._menu_service.get_menu_content(id=id)

    def get_recommendation_by_menu(self, request, allergens: Filters = Query(...)) -> MenuOut:
        return self._recommendation_service.get_recommendation_by_menu(allergens=allergens)

    def get_recommendation_on_day(self, request, rec_filter: RecommendationFilter = Query(...)) -> RecommendationOnDay:
        return self._recommendation_service.get_recommendation_on_day(rec_filter=rec_filter)

    def get_recommendation_on_week(self, request,
                                   rec_filter: RecommendationFilter = Query(...)) -> List[RecommendationOnDay]:
        return self._recommendation_service.get_recommendation_on_week(rec_filter=rec_filter)
