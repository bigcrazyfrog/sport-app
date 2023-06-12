from ninja import NinjaAPI

from app.internal.allergens.db.repositories import AllergenRepository
from app.internal.allergens.domain.services import AllergenService
from app.internal.allergens.presentation.handlers import AllergenHandlers
from app.internal.allergens.presentation.routers import add_allergens_router
from app.internal.exceptions.default import NotFoundException
from app.internal.menus.db.repositories import MenuRepository
from app.internal.menus.domain.services import MenuService
from app.internal.menus.presentation.handlers import MenuHandlers
from app.internal.menus.presentation.routers import add_menus_router
from app.internal.products.db.repositories import ProductRepository
from app.internal.products.domain.services import ProductService
from app.internal.products.presentation.handlers import ProductHandlers
from app.internal.products.presentation.routers import add_products_router
from app.internal.recommendations.db.repositories import RecommendationRepository
from app.internal.recommendations.domain.services import RecommendationService


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
