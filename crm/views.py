from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer, Address, Order
from django.views.generic import ListView, DetailView, FormView
from .forms import CustomerForm


class CustomerList(LoginRequiredMixin, ListView, FormView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm/crm_customers.html'
    success_url = '/crm'
    login_url = '/auth/login/'

    def form_valid(self, form):
        form.save()
        return super(CustomerList, self).form_valid(form)


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'crm/crm_customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(customer_id=self.kwargs['pk'])
        context['address_list'] = Address.objects.filter(customer=self.kwargs['pk'])
        return context


class AddressList(ListView):
    model = Address
    template_name = 'crm/crm_addresses.html'


class OrderList(ListView):
    model = Order
    template_name = 'crm/crm_orders.html'
