from django.urls import path,include
from . import views

urlpatterns = [
    path('relation/', views.RelationHome, name='relation'),
     path('relation/<int:pk>',views.RelationDetail,name="book_detail"),
    path('relation/addpublisher/', views.addpublisher, name='addPublisher'),
]