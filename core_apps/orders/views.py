from django.urls import reverse_lazy
from django.views.generic import CreateView

from core_apps.common.mixins import SetUserMixin

from .forms import OrderForm
from .models import Order


class OrderCreateView(SetUserMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("orders:add_order")
