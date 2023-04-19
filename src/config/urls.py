from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('sport/', include('app.internal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)