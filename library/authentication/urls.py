from django.urls import path

from . import views

app_name = "authentication"
urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("users/<int:user_id>", views.show_user, name="show_user"),
    path("users/<int:user_id>/books", views.show_user_books, name="user_books"),
]
