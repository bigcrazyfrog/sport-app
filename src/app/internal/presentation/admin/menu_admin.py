from django.contrib import admin

from app.internal.db.models.menu import Menu, Recommendation


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ["menu", "day", "breakfast", "lunch", "dinner", "kalo_sum"]
    readonly_fields = ("kalo_sum",)
