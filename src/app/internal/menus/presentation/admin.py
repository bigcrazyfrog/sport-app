from django.contrib import admin

from app.internal.menus.db.models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    pass
