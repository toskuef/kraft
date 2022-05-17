from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, FormView
from django.db.models import Sum

from .models import Nomenclature, Contractor, Category, Purchase, Storage, Specification
from .forms import NomenclatureForm


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


class NeedView(ListView):
    model = Nomenclature
    template_name = 'supply/supply_purchase.html'

    def get_queryset(self):
        return Nomenclature.objects.filter(specification__is_booking=False).annotate(total=Sum('specification__count'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        purchases = Nomenclature.objects.filter(specification__is_booking=True).annotate(total=Sum('specification__count'))
        context['purchases'] = purchases
        specification = Specification.objects.all()
        context['specification'] = specification
        storage_id = self.kwargs.get('storage_id')
        context['storage_id'] = storage_id
        return context


@csrf_exempt
def is_not_order(request):
    if request.method == 'POST':
        need_id = request.POST.get('need_id')
        Drag.objects.filter(pk=drag_id).update(name_2='first')
    object_list = Drag.objects.all()
    return render(request, 'drag/add_drag.html', {'object_list': object_list})

@csrf_exempt
def is_order(request):
    if request.method == 'POST':
        drag_id = request.POST.get('drag_id')
        Drag.objects.filter(pk=drag_id).update(name_2='second')
    object_list = Drag.objects.all()
    return render(request, 'drag/drag.html',
                  {'object_list': object_list})


@csrf_exempt
def is_booking(request):
    ids = request.POST.getlist('ids')
    Specification.objects.filter(pk__in=ids).update(is_booking=True)
    specification = Specification.objects.all()
    context = {'specification': specification}
    return render(request, 'supply/includes/supply_modal_is_booking.html', context)
    # return render(request, 'drag/add_drag.html', {'object_list': object_list})

@csrf_exempt
def is_not_booking(request):
    ids = request.POST.getlist('ids')
    Specification.objects.filter(pk__in=ids).update(is_booking=False)
    specification = Specification.objects.all()
    context = {'specification': specification}
    return render(request, 'supply/includes/supply_modal_is_booking.html', context)

