from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

app_name = "book"
urlpatterns = [
    path("", views.all_books, name="all_books"),
    path("<int:book_id>", views.specific_book, name="specific_book"),
    path("filter", views.filter_books, name="filter_books"),
]
