from typing import List

from app.internal.menus.domain.entities import MenuContentOut, MenuOut


class IMenuRepository:
    def get_menu_by_id(self, id: int) -> MenuOut:
        ...

    def get_menu_list(self) -> List[MenuOut]:
        ...

    def get_menu_content(self, id: int) -> List[MenuContentOut]:
        ...


class MenuService:
    def __init__(self, menu_repo: IMenuRepository):
        self._menu_repo = menu_repo

    def get_menu_by_id(self, id: int) -> MenuOut:
        return self._menu_repo.get_menu_by_id(id=id)

    def get_menu_list(self) -> List[MenuOut]:
        return self._menu_repo.get_menu_list()

    def get_menu_content(self, id: int) -> List[MenuContentOut]:
        return self._menu_repo.get_menu_content(id=id)
