from django.shortcuts import render
from .models import *
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


def gallery(request, page_number):
    context = {}
    page_number = int(page_number)
    if page_number < 1:
        page_number = 1
    if 'search_word' in request.GET:
        search_word = request.GET['search_word']
        image_list = Image.objects.filter(title__icontains=search_word)
        context['search_word'] = search_word
    else:
        image_list = Image.objects.all()
    image_list = image_list.order_by('-number')
    image_list_length = image_list.count()
    max_page_number = math.ceil(image_list_length / 12)
    if page_number > max_page_number:
        page_number = max_page_number
    if image_list_length == 0:
        image_list_sliced = []
    else:
        image_list_sliced = image_list[(page_number - 1) * 12:min([page_number * 12, image_list_length])]
    image_title_filename_list = [(img.title, img.get_filename()) for img in image_list_sliced]
    context['image_title_filename_list'] = image_title_filename_list
    context['pages'] = [(x + 1) for x in range(max_page_number)]
    context['current_page'] = page_number
    context['previous_page'] = max([page_number - 1, 1])
    context['next_page'] = min([page_number + 1, len(context['pages'])])
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
    max_page_number = math.ceil(review_list_length / 10)
    if page_number > max_page_number:
        page_number = max_page_number
    if review_list_length == 0:
        review_list_sliced = []
    else:
        review_list_sliced = review_list[(page_number-1)*10:min([page_number*10, review_list_length])]
    context['reviews'] = review_list_sliced
    context['pages'] = [(x+1) for x in range(max_page_number)]
    context['current_page'] = page_number
    context['previous_page'] = max([page_number - 1, 1])
    context['next_page'] = min([page_number + 1, len(context['pages'])])
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
