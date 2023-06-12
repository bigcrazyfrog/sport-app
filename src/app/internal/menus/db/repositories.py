from typing import Optional, List

from app.internal.exceptions.default import NotFoundException
from app.internal.menus.db.models import Menu, Recommendation
from app.internal.menus.domain.entities import MenuOut, MenuContentOut
from app.internal.menus.domain.services import IMenuRepository


class MenuRepository(IMenuRepository):
    def get_menu_by_id(self, id: int) -> MenuOut:
        menu: Optional[Menu] = Menu.objects.filter(id=id).first()
        if menu is None:
            raise NotFoundException(name="Menu", id=id)

        return MenuOut.from_orm(menu)

    def get_menu_list(self) -> List[MenuContentOut]:
        return Menu.objects.all()

    def get_menu_content(self, id: int) -> List[MenuContentOut]:
        content = Recommendation.objects.filter(menu__id=id).order_by("day")
        if len(content) == 0:
            raise NotFoundException(name="Menu", id=id)

        return content
