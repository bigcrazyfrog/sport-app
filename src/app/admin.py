from django.contrib import admin

from app.internal.presentation.admin.product_admin import ProductAdmin
from app.internal.presentation.admin.menu_admin import MenuAdmin, RecommendationAdmin
from app.internal.presentation.admin.allergen_admin import AllergenAdmin

admin.site.site_title = "Backend sport"
admin.site.site_header = "Backend sport"
