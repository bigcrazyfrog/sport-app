from ninja import NinjaAPI

from app.internal.db.repositories.allergen_repo import AllergenRepository
from app.internal.db.repositories.menu_repo import MenuRepository
from app.internal.db.repositories.product_repo import ProductRepository
from app.internal.db.repositories.recommendation_repo import RecommendationRepository
from app.internal.domain.entities.entities import NotFoundException
from app.internal.domain.services.allergen_service import AllergenService
from app.internal.domain.services.menu_services import MenuService
from app.internal.domain.services.product_service import ProductService
from app.internal.domain.services.recomendation_services import RecommendationService
from app.internal.presentation.handlers.allergen_handlers import AllergenHandlers
from app.internal.presentation.handlers.menu_handlers import MenuHandlers
from app.internal.presentation.handlers.product_handlers import ProductHandlers
from app.internal.presentation.routers.allergen_routers import add_allergens_router
from app.internal.presentation.routers.menu_routers import add_menus_router
from app.internal.presentation.routers.product_routers import add_products_router


def get_api():
    api = NinjaAPI(
        title='SPORT.BACKEND',
        version='1.0.1',
        auth=None,
    )

    product_repo = ProductRepository()
    product_service = ProductService(product_repo=product_repo)
    product_handlers = ProductHandlers(product_service=product_service)
    add_products_router(api, product_handlers)

    allergen_repo = AllergenRepository()
    allergen_service = AllergenService(allergen_repo=allergen_repo)
    allergen_handlers = AllergenHandlers(allergen_service=allergen_service)
    add_allergens_router(api, allergen_handlers)

    menu_repo = MenuRepository()
    recommendation_repo = RecommendationRepository()
    menu_service = MenuService(menu_repo=menu_repo)
    recommendation_service = RecommendationService(recommendation_repo=recommendation_repo)
    menu_handlers = MenuHandlers(menu_service=menu_service, recommendation_service=recommendation_service)
    add_menus_router(api, menu_handlers)

    return api


product_api = get_api()


@product_api.exception_handler(NotFoundException)
def not_found_exception_handler(request, exc):
    return product_api.create_response(
        request,
        {"message": f"{exc.name} with id {exc.id} not found"},
        status=404,
    )
