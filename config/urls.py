from autocomplete import HTMXAutoComplete
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("core_apps.books.urls")),
    path("", include("core_apps.orders.urls")),
    *HTMXAutoComplete.url_dispatcher("ac"),
]
