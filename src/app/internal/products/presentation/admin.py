from django.contrib import admin

from app.internal.products.db.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "kilocalories", "proteins", "fats", "carb", "proportion"]
