from django.urls import path,include
from . import views

urlpatterns = [
    path('relation/', views.RelationHome, name='relation'),
    
]
