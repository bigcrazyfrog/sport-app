from django.contrib import admin

from app.internal.admin_users.presentation.admin import AdminUserAdmin
from app.internal.allergens.presentation.admin import AllergenAdmin
from app.internal.menus.presentation.admin import MenuAdmin
from app.internal.products.presentation.admin import ProductAdmin
from app.internal.recommendations.presentation.admin import RecommendationAdmin

admin.site.site_title = "Backend sport"
admin.site.site_header = "Backend sport"
