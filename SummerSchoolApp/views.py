from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


def base(request):
    context = {}
    return render(request, 'base.html', context)


def gallery(request):
    context = {}
    return render(request, 'gallery.html', context)


def faq(request):
    context = {}
    return render(request, 'faq.html', context)
