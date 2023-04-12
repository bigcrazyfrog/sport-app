from django.contrib import admin

from app.internal.models.allergens import Allergen


@admin.register(Allergen)
class AllergenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
