from django.urls import path
from .views import list_users, my_orders, create_order

urlpatterns = [
    path('users/', list_users, name='list_users'),
    path('my_orders/', my_orders, name='my_orders'),
    path('create_order/', create_order, name='create_order'),
]