from django.shortcuts import render


def index(request):
    template = 'main/index.html'
    return render(request, template)


def test(request):
    template = 'main/test.html'
    return render(request, template)
