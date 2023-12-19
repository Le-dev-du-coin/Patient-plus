from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("core.urls")),
    path("patient/", include("patient.urls")),
    path("docteur/", include("doctor.urls")),
    path("compte/", include("authentication.urls")),
    path("admin/", admin.site.urls),
]


# Media and static files settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
