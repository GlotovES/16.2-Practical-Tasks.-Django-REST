# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import viewsets
from .models import User, Order, Book, Author
from .serializers import  BookSerializer
from .models import Book


def all_books(request):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    books = Book.get_all()
    context = {"books": books, "filter": False}
    return render(request, "book/books.html", context=context)


def specific_book(request, book_id):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    book = Book.get_by_id(book_id)
    context = {"book": book}
    return render(request, "book/book.html", context=context)


def filter_books(request):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    filter_conditions = {}

    title = request.GET.get("title")
    if title:
        filter_conditions["name__icontains"] = title

    author = request.GET.get("author")
    if author:
        filter_conditions["author"] = author

    count_min = request.GET.get("count_min")
    if count_min:
        filter_conditions["count__gte"] = count_min

    count_max = request.GET.get("count_max")
    if count_max:
        filter_conditions["count__lte"] = count_max

    books = Book.objects.filter(**filter_conditions)
    context = {"books": books, "filter": True}
    return render(request, "book/books.html", context=context)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
