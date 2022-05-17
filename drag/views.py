from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView
from .models import Drag

@csrf_exempt
def post(request):
    if request.method == 'POST':
        drag_id = request.POST.get('drag_id')
        Drag.objects.filter(pk=drag_id).update(name_2='first')
    object_list = Drag.objects.all()
    return render(request, 'drag/add_drag.html', {'object_list': object_list})

@csrf_exempt
def post_2(request):
    if request.method == 'POST':
        drag_id = request.POST.get('drag_id')
        Drag.objects.filter(pk=drag_id).update(name_2='second')
    object_list = Drag.objects.all()
    return render(request, 'drag/drag.html',
                  {'object_list': object_list})


def add_drag(request):
    print(request.POST)
    name = request.POST.get('drag_name')
    Drag.objects.create(name=name)
    object_list = Drag.objects.all()
    return render(request, 'drag/add_drag.html', {'object_list': object_list})


def del_drag(request, pk):
    Drag.objects.filter(pk=pk).delete()
    object_list = Drag.objects.all()
    return render(request, 'drag/add_drag.html', {'object_list': object_list})

class DragView(ListView):
    template_name = 'drag/index.html'
    model = Drag
