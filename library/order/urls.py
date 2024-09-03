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