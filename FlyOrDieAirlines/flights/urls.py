from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = "flights"

urlpatterns = [
    path("", views.home, name = 'home' ),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
]