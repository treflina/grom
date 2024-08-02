from django.urls import path

from .views import OrderCreateView

app_name = "orders"

urlpatterns = [
    path("zamowienia/dodaj/", OrderCreateView.as_view(), name="order_add")
]
