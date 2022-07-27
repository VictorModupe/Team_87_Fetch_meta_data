from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("login", view=views.login, name="login"),
    path("register", view=views.register, name="register"),
    path("metadata", view=views.metadata, name="metadata"),
    path("user", view=views.user, name="user")
]
