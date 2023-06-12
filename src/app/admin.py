from django.contrib import admin

from app.internal.products.presentation.admin import ProductAdmin
from app.internal.menus.presentation.admin import MenuAdmin, RecommendationAdmin
from app.internal.allergens.presentation.admin import AllergenAdmin
from app.internal.admin_users.presentation.admin import AdminUserAdmin

admin.site.site_title = "Backend sport"
admin.site.site_header = "Backend sport"
