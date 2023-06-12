from django.contrib import admin

from app.internal.allergens.db.models import Allergen


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
