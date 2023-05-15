from typing import List

from app.internal.domain.entities.menu_entities import MenuOut, MenuContentOut, Filters, RecommendationFilter, \
    RecommendationOnDay


class IRecommendationRepository:
    def get_recommendation_by_menu(self, id: int) -> MenuOut:
        ...

    def get_recommendation_on_day(self, rec_filter: RecommendationFilter) -> RecommendationOnDay:
        ...

    def get_recommendation_on_week(self, rec_filter: RecommendationFilter) -> List[RecommendationOnDay]:
        ...


class RecommendationService:
    def __init__(self, recommendation_repo: IRecommendationRepository):
        self._recommendation_repo = recommendation_repo

    def get_recommendation_by_menu(self, allergens: Filters) -> MenuOut:
        return self._recommendation_repo.get_recommendation_by_menu(allergens=allergens)

    def get_recommendation_on_day(self, rec_filter: RecommendationFilter) -> RecommendationOnDay:
        return self._recommendation_repo.get_recommendation_on_day(rec_filter=rec_filter)

    def get_recommendation_on_week(self, rec_filter: RecommendationFilter) -> List[RecommendationOnDay]:
        return self._recommendation_repo.get_recommendation_on_week(rec_filter=rec_filter)
