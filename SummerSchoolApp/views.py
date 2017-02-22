from django.shortcuts import render
from .models import Review
from django.db.models import Q
import math


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


def review(request, page_number):
    context = {}
    page_number = int(page_number)
    if page_number < 1:
        page_number = 1
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        query = Q(student__icontains=search_word) | Q(title__icontains=search_word) | Q(content__icontains=search_word)
        review_list = Review.objects.filter(query)
        context['search_word'] = search_word
    else:
        review_list = Review.objects.all()
    review_list = review_list.order_by('-number')
    review_list_length = review_list.count()
    review_list_sliced = review_list[(page_number-1)*10:min([page_number*10, review_list_length])]
    context['reviews'] = review_list_sliced
    context['pages'] = [(x+1) for x in range(math.ceil(review_list_length / 10))]
    context['current_page'] = page_number
    context['previous_page'] = page_number - 1
    context['next_page'] = page_number + 1
    print(review_list_length)
    print(context['pages'])
    return render(request, 'review.html', context)


def review_one(request, number):
    context = {}
    context['review'] = Review.objects.filter(number=number)[0]
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
