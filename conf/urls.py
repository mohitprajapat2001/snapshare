from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from conf.views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("", include("snap.urls", namespace="snap")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
