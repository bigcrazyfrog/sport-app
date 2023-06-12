from typing import List

from ninja import NinjaAPI, Router

from app.internal.menus.domain.entities import MenuOut, MenuContentOut
from app.internal.menus.presentation.handlers import MenuHandlers
from app.internal.recommendations.domain.entities import RecommendationOnDay
from app.internal.responses.default import ErrorResponse, NotFoundResponse


def get_menus_router(menu_handlers: MenuHandlers):
    router = Router(tags=['menus'])

    router.add_api_operation(
        '',
        ['GET'],
        menu_handlers.get_menu_list,
        response={200: List[MenuOut], 400: ErrorResponse},
        description="Get a list of all menus",
    )

    router.add_api_operation(
        '/{int:id}',
        ['GET'],
        menu_handlers.get_menu_by_id,
        response={200: MenuOut, 404: NotFoundResponse},
        description="Get the menu by a unique identifier",
    )

    router.add_api_operation(
        '/content',
        ['GET'],
        menu_handlers.get_menu_content,
        response={200: List[MenuContentOut], 404: NotFoundResponse},
        description="Get the menu content by a unique identifier",
    )

    router.add_api_operation(
        '/recommendation',
        ['GET'],
        menu_handlers.get_recommendation_by_menu,
        response={200: MenuOut, 404: NotFoundResponse},
        description="Get the menu content by a unique identifier",
    )

    router.add_api_operation(
        '/recommendation/day',
        ['GET'],
        menu_handlers.get_recommendation_on_day,
        response={200: RecommendationOnDay, 404: NotFoundResponse},
        description="Get the menu content by a unique identifier",
    )

    router.add_api_operation(
        '/recommendation/week',
        ['GET'],
        menu_handlers.get_recommendation_on_week,
        response={200: List[RecommendationOnDay], 404: NotFoundResponse},
        description="Get the menu content by a unique identifier",
    )

    return router


def add_menus_router(api: NinjaAPI, menu_handlers: MenuHandlers):
    api.add_router('/menus', get_menus_router(menu_handlers))
