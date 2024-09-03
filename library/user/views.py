from rest_framework import viewsets
from .models import User, Order, Book, Author
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer