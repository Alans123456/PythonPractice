from django.shortcuts import render
from .models import Book

# Create your views here.
def LibraryHome(request):
    user = request.user
    book = Book.objects.all()
    return render(request,'Library.html',{'book':book,'user':user})

