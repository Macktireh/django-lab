from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django_view_decorator import include_view_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("unicorn/", include("django_unicorn.urls")),
    path("stripe/", include("djstripe.urls", namespace="djstripe")),
    path("", include_view_urls()),
]

if settings.DEBUG:
    urlpatterns.append(path("__reload__/", include("django_browser_reload.urls")))
