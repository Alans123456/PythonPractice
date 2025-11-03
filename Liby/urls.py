from django.urls import path
from . import views

urlpatterns = [
    path('library', views.LibraryHome, name='library'),
]
