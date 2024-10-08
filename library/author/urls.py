from django.urls import path
from .views import list_users, my_orders, create_order
from .views import UserViewSet, OrderViewSet, BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'order', OrderViewSet)
router.register(r'book', BookViewSet)
router.register(r'author', AuthorViewSet)



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('users/', list_users, name='list_users'),
    path('my_orders/', my_orders, name='my_orders'),
    path('create_order/', create_order, name='create_order'),
]