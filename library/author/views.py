from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import  Author
from .serializers import AuthorSerializer


def list_users(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer