from django.contrib import admin

from app.internal.models.products import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'proteins', 'fats', 'carb')
