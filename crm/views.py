from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render

from .models import (Customer, Address, Order, StatusOrder, Product,
                     Measuring, Project, Task)
from django.views.generic import ListView, DetailView, FormView
from .forms import (CustomerForm, OrderForm, CommentForm, ProductForm,
                    MeasuringForm, ProjectForm, TaskForm)
from django.db.models import Q
from production.models import ProductOrder
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

from .services.services import get_context_comm_window, get_customer_orders, \
    get_customer_addresses, Vkontakte

token = 'e132b726def62984bb229e1feb5d4226d7ac8c6259c427c41a198407818198d78d655468ef17b8195a968'
group_token = '8f9048a4892d2b9a82f14827dea55306849825156c574ad52c9044718b64ee8f085dcdd983da5230d0dac'

ACTIONS = [['Комментарий', 'comment'], ['Задача', 'task'], ['VK', 'VK']]


class CustomerList(ListView):
    model = Customer
    template_name = 'crm/crm_customers.html'

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        if search_query:
            return self.model.objects.filter(Q(last_name__iregex=search_query))
        return Customer.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = CustomerForm
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = CustomerForm(request.POST)
            if form.is_valid():
                customer = form.save(commit=False)
                customer.creater_customer = request.user
                customer.save()
                return redirect('crm:crm_customers')
            return render(request, 'crm/crm_customers.html', {
                'object_list': Customer.objects.all(),
                'form': form,
                'show': 'show',
            })


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'crm/crm_customer_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer_id = self.kwargs['pk']
        context['new_comment'] = CommentForm
        context['new_task'] = TaskForm
        # context['address_list'] = get_customer_addresses(customer_id)
        context['new_order'] = OrderForm
        context['actions'] = ACTIONS
        context['order_list'] = get_customer_orders(customer_id)
        context['select'] = 'comment'
        context.update(get_context_comm_window(Customer, customer_id))
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            template = 'crm/includes/crm_communication_window.html'
            if 'title' in request.POST:
                form = OrderForm(request.POST)
                customer = self.kwargs.get('pk')
                form_add_customer = form.save(commit=False)
                form_add_customer.customer = Customer.objects.get(pk=customer)
                form.save()
                return redirect('crm:crm_customer_detail', pk=customer)
            if 'last_name' in request.POST:
                customer = self.kwargs.get('pk')
                instance = get_object_or_404(Customer, pk=customer)
                form = CustomerForm(request.POST, instance=instance)
                form.save()
                return redirect('crm:crm_customer_detail', pk=customer)
            customer = Customer.objects.get(pk=self.kwargs['pk'])
            if 'text' in request.POST:
                form = CommentForm(request.POST)
                comment = form.save(commit=False)
                comment.content_object = customer
                comment.staff = request.user
                comment.save()
                context = get_context_comm_window(Customer, self.kwargs['pk'])
                return render(request, template, context)
            if 'task' in request.POST:
                form = TaskForm(request.POST)
                task = form.save(commit=False)
                task.content_object = customer
                task.staff = request.user
                task.save()
                context = get_context_comm_window(Customer, self.kwargs['pk'])
                return render(request, template, context)
            if 'done_task' in request.POST:
                task_id = request.POST['done_task']
                Task.objects.filter(pk=task_id).update(is_done=True)
                return redirect('crm:crm_customer_detail',
                                pk=self.kwargs['pk'])
            if 'vk' in request.POST:
                answer = request.POST['vk']
                vk_session = vk_api.VkApi(token=group_token)
                vk = vk_session.get_api()
                print(customer.social_web.get(name_social=2))
                vk.messages.send(
                    user_id=customer.social_web.get(name_social=2),
                    random_id=get_random_id(),
                    message=answer
                )
                context = get_context_comm_window(Customer, self.kwargs['pk'])
                return render(request, template, context)

    def render_new_message(self):
        request = self.request
        template = 'crm/includes/crm_communication_window.html'
        context = get_context_comm_window(Customer, self.kwargs['pk'])
        return render(request, template, context)




def get_form_communication(request):
    if request.method == 'GET':
        templates = {
            'comment': 'crm/includes/crm_form_communication/crm_comment.html',
            'task': 'crm/includes/crm_form_communication/crm_task.html',
            'VK': 'crm/includes/crm_form_communication/crm_vk.html'}
        action = request.GET['action']
        if action == 'comment':
            return render(request, templates[action],
                          {'new_comment': CommentForm})
        if action == 'task':
            return render(request, templates[action], {'new_task': TaskForm})
        if action == 'VK':
            return render(request, templates[action])


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)
    context = {'customer': customer, 'edit_customer': form}
    template_name = 'crm/crm_customer_edit.html'
    return render(request, template_name, context)


def new_task(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = TaskForm
    context = {'customer': customer, 'new_task': form}
    template_name = 'crm/crm_new_task.html'
    return render(request, template_name, context)


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

    def get_context_data(self, *args, **kwargs):
        context = super(OrderList, self).get_context_data(*args, **kwargs)
        context['status_order'] = StatusOrder.objects.all()
        context['products'] = Product.objects.all()
        return context


class OrderDetail(DetailView):
    model = Order
    template_name = 'crm/crm_order_detail.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        order = Order.objects.get(pk=self.kwargs['pk'])
        context['tasks'] = order.tasks.all()
        context['comments'] = order.comments.all()
        context['new_comment'] = CommentForm
        context['new_task'] = TaskForm
        context['new_product'] = ProductForm
        context['products'] = Product.objects.filter(order=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            order = Order.objects.get(pk=self.kwargs['pk'])
            if 'text' in request.POST:
                form = CommentForm(request.POST)
                comment = form.save(commit=False)
                comment.content_object = order
                comment.staff = request.user
                comment.save()
                return redirect('crm:crm_order_detail', pk=self.kwargs['pk'])
            if 'task' in request.POST:
                print(request.POST)
                form = TaskForm(request.POST)
                task = form.save(commit=False)
                task.content_object = order
                task.staff = request.user
                task.save()
                return redirect('crm:crm_order_detail', pk=self.kwargs['pk'])
            if 'title' in request.POST:
                form = ProductForm(request.POST)
                product = form.save(commit=False)
                product.order = order
                product.save()
                return redirect('crm:crm_order_detail', pk=self.kwargs['pk'])
            if 'status_order' in request.POST:
                Order.objects.filter(pk=self.kwargs['pk']).update(
                    status_order=3)
                products = Product.objects.filter(order=order)
                product_in_product_order = [ProductOrder(
                    name=product,
                    is_active=True,
                    is_specification_done=False
                ) for product in products]
                ProductOrder.objects.bulk_create(product_in_product_order)
                return redirect('crm:crm_order_detail', pk=self.kwargs['pk'])


class ProductDetail(DetailView):
    model = Product
    template_name = 'crm/crm_product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['new_measuring'] = MeasuringForm
        context['new_project'] = ProjectForm
        context['measurings'] = Measuring.objects.filter(
            product=self.kwargs['pk'])
        context['projects'] = Project.objects.filter(
            product=self.kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'measuring' in request.FILES:
                form = MeasuringForm(request.POST, request.FILES)
                measuring = form.save(commit=False)
                measuring.product = Product.objects.get(pk=self.kwargs['pk'])
                measuring.save()
                return redirect('crm:crm_product_detail', pk=self.kwargs['pk'])
            if 'project' in request.FILES:
                form = ProjectForm(request.POST, request.FILES)
                project = form.save(commit=False)
                project.product = Product.objects.get(pk=self.kwargs['pk'])
                project.save()
                return redirect('crm:crm_product_detail', pk=self.kwargs['pk'])
