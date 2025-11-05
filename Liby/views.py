from django.shortcuts import render
from .models import Book

# Create your views here.
def LibraryHome(request):
    user = request.user
    books = Book.objects.all()
    return render(request,'Library.html',{'books':books,'user':user})

