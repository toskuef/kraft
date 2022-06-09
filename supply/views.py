from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView
from django.db.models import Sum
from django.views.generic.edit import FormMixin

from .models import Nomenclature, Contractor, Category, Purchase, Storage, Specification
from .forms import NomenclatureForm, NeedConfirmForm


class NomenclatureList(ListView, FormView):
    model = Nomenclature
    template_name = 'supply/supply_nomenclature.html'
    form_class = NomenclatureForm
    success_url = '/supply'

    def form_valid(self, form):
        form.save()
        return super(NomenclatureList, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        storages = Storage.objects.all()
        context['storages'] = storages
        storage_id = self.kwargs.get('storage_id')
        context['storage_id'] = storage_id
        return context


def group(request):
    form = NomenclatureForm(request.GET)
    return HttpResponse(form['group'])


class ContractorListView(ListView):
    model = Contractor
    template_name = 'supply/supply_contractors.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        storages = Storage.objects.all()
        context['storages'] = storages
        storage_id = self.kwargs.get('storage_id')
        context['storage_id'] = storage_id
        return context


class StorageListView(ListView):
    model = Nomenclature
    template_name = 'supply/supply_storage.html'

    def get_queryset(self):
        return Nomenclature.objects.filter(purchase__storage=self.kwargs.get('storage_id')).annotate(total=Sum('purchase__count'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Purchase.objects.all()
        context['purchases'] = purchases
        storages = Storage.objects.all()
        context['storages'] = storages
        storage_id = self.kwargs.get('storage_id')
        context['storage_id'] = storage_id
        return context


class NeedView(ListView, FormView):
    model = Nomenclature
    template_name = 'supply/supply_purchase.html'
    form_class = NeedConfirmForm
    success_url = '/supply/need'

    def form_valid(self, form):
        form.save()
        return super(NeedView, self).form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     print(request.POST)
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def get_queryset(self):
        return Nomenclature.objects.filter(specification__is_booking=False,
                                           specification__is_order=False
                                           ).annotate(total=Sum('specification__count'))

    def get_context_data(self, *args, **kwargs):
        context = super(NeedView, self).get_context_data(*args, **kwargs)
        purchases = Nomenclature.objects.filter(specification__is_booking=True,
                                                specification__is_order=False
                                                ).annotate(total=Sum('specification__count'))
        context['purchases'] = purchases
        specification = Specification.objects.all()
        context['specification'] = specification
        contractors = Contractor.objects.all()
        context['contractors'] = contractors
        storages = Storage.objects.all()
        context['storages'] = storages
        storage_id = self.kwargs.get('storage_id')
        context['storage_id'] = storage_id
        return context


def need_list_confirm_is_not_booking(request, need_id):
    if request.method == "POST":
        print(request.POST)
        ids = request.POST.getlist('ids')
        Specification.objects.filter(pk__in=ids).update(is_booking=True)
        return redirect('supply:supply_purchase')
    specification = Specification.objects.filter(nomenclature=need_id,
                                                 is_booking=False,
                                                 is_order=False)
    return render(request, 'supply/includes/supply_modal_is_booking.html',
                  {'specification': specification})


def need_list_confirm_is_booking(request, need_id):
    if request.method == "POST":
        print(request.POST)
        ids = request.POST.getlist('ids')
        Specification.objects.filter(pk__in=ids).update(is_booking=False)
        return redirect('supply:supply_purchase')
    specification = Specification.objects.filter(nomenclature=need_id,
                                                 is_booking=True,
                                                 is_order=False)
    return render(request, 'supply/includes/supply_modal_is_booking.html',
                  {'specification': specification})


def create_supply_order(request):
    contractor = request.POST.get('contractor')
    nom = Nomenclature.objects.filter(specification__is_booking=True,
                                      specification__is_order=False).annotate(
        total=Sum('specification__count')).values('pk', 'total')
    order_for_supply = [Purchase(
        nomenclature=Nomenclature.objects.get(pk=order.get('pk')),
        contractor=Contractor.objects.get(pk=contractor),
        count=order.get('total'),
    ) for order in nom]
    print(order_for_supply)
    Purchase.objects.bulk_create(order_for_supply)
    Specification.objects.filter(is_booking=True).update(is_order=True)
    return redirect('supply:supply_purchase')


