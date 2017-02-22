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


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def review(request):
    context = {}
    return render(request, 'review.html', context)


def review_one(request):
    context = {}
    return render(request, 'review_one.html', context)


def dates(request):
    context = {}
    return render(request, 'dates.html', context)


def track1(request):
    context = {}
    return render(request, 'track1.html', context)


def track2(request):
    context = {}
    return render(request, 'track2.html', context)
