from django.conf import settings  # type: ignore
from django.conf.urls.static import static  # type: ignore
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

urlpatterns = [
    path("", include("core.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("items/", include("item.urls")),
    path("conversation/", include("conversation.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
