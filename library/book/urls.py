from django.urls import path

from . import views

app_name = "book"
urlpatterns = [
    path("", views.all_books, name="all_books"),
    path("<int:book_id>", views.specific_book, name="specific_book"),
    path("filter", views.filter_books, name="filter_books"),
]
