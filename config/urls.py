from django.contrib import admin
from django.urls import include, path
from django_view_decorator import include_view_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path("", include_view_urls()),
]
