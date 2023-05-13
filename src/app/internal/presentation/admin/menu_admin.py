from django.contrib import admin

from app.internal.db.models.menu import Menu, Recommendation


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    pass


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ["menu", "day", "get_breakfast", "get_lunch", "get_dinner", "kalo_sum"]
    filter_horizontal = ("breakfast", "lunch", "dinner")
    readonly_fields = ("kalo_sum",)

    def get_breakfast(self, obj):
        return ",\n".join([p.name for p in obj.breakfast.all()])

    def get_lunch(self, obj):
        return ",\n".join([p.name for p in obj.lunch.all()])

    def get_dinner(self, obj):
        return ",\n".join([p.name for p in obj.dinner.all()])
