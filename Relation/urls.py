from django.urls import path
from . import views

app_name = 'relation'

urlpatterns = [
    path('relation/', views.RelationHome, name='home'),
    path('relation/<int:pk>/', views.book_detail, name='book_detail'),
    path('relation/addpublisher/', views.addpublisher, name='addpublisher'),
    path('verify-khalti-payment/', views.verify_khalti_payment, name='verify_payment'),
]