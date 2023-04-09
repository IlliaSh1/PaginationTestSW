from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator

from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("Home")


def pagination(request, page):
    book_list = Book.objects.all()
    paginator = Paginator(book_list, 2)

    page_num = page
    page_obj = paginator.get_page(page_num)
    return render(request, 'pagination/pagination.html', {'page_obj': page_obj})
