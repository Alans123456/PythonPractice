from django.urls import path
from . import views

urlpatterns = [
   path("", views.SignUpPage, name="signup"),
   path("login", views.LoginPage, name="login"),
   # path("libray", views.LibraryPage, name="library"),
]