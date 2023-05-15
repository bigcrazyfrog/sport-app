from django.contrib import admin

from app.internal.db.models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "kilocalories", "proteins", "fats", "carb", "proportion"]
