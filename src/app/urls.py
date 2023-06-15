from django.contrib import admin
from django.urls import path

from app.internal.app import product_api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", product_api.urls),
]
