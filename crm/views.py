from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer, Address, Order
from django.views.generic import ListView, DetailView, FormView
from .forms import CustomerForm, OrderForm
from django.db.models import Q


class CustomerList(LoginRequiredMixin, ListView, FormView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm/crm_customers.html'
    success_url = '/crm'
    # login_url = '/auth/login/'

    def form_valid(self, form):
        form.save()
        return super(CustomerList, self).form_valid(form)

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return self.model.objects.filter(Q(last_name__iregex=search_query))
        return Customer.objects.all()


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


class OrderList(ListView, FormView):
    model = Order
    template_name = 'crm/crm_orders.html'
    form_class = OrderForm
    success_url = '/crm/orders'

    def form_valid(self, form):
        form.save()
        return super(OrderList, self).form_valid(form)
