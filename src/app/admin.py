from django.contrib import admin

from app.internal.admin.admin_allergens import AllergenAdmin
from app.internal.admin.admin_products import ProductAdmin
from app.internal.admin.admin_user import AdminUserAdmin

admin.site.site_title = "Backend sport"
admin.site.site_header = "Backend sport"
