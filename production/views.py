from django.views.generic import FormView, ListView

from .models import ProductOrder
from .forms import OrderForm


class OrderList(ListView, FormView):
    model = ProductOrder
    template_name = 'production/production_orders.html'
    form_class = OrderForm
    success_url = '/production/orders'

    def form_valid(self, form):
        form.save()
        return super(OrderList, self).form_valid(form)
