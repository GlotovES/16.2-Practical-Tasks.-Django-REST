# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


def home(request):
    return render(request, "authentication/home.html")


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        middle_name = request.POST.get("middle_name")
        last_name = request.POST.get("last_name")
        if request.POST.get("role") == "on":
            role = 1
            user = CustomUser.create(
                email, password, role, first_name, middle_name, last_name
            )
            user.is_superuser = True
            user.is_staff = True
            user.save()
        else:
            role = 0
            user = CustomUser.create(
                email, password, role, first_name, middle_name, last_name
            )
        return redirect(reverse("authentication:login"))
    return render(request, "authentication/register.html")


def log_in(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user.is_active = True
            user.save()
            return redirect(reverse("authentication:home"))
    return render(request, "authentication/log_in.html")


def log_out(request):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    request.user.is_active = False
    request.user.save()
    logout(request)
    return redirect(reverse("authentication:home"))


def show_user(request, user_id):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    user = CustomUser.get_by_id(user_id)
    context = {"user": user}
    return render(request, "authentication/user.html", context=context)


def show_user_books(request, user_id):
    if not request.user.is_active:
        return redirect(reverse("authentication:login"))
    if request.user.is_superuser or request.user.id == user_id:
        user = CustomUser.get_by_id(user_id)
        books = user.books.all()
        context = {"books": books, "user_name": user.first_name, "filter": False}
        return render(request, "book/books.html", context=context)
    else:
        return redirect(reverse("book:all_books"))
