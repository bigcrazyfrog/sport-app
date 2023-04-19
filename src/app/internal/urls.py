from django.contrib import admin
from django.urls import include, path

from app.internal.transport.rest.handlers import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
