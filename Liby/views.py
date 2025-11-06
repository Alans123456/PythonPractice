from django.shortcuts import render,redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse

# Create your views here.
def LibraryHome(request):
    user = request.user
    book = Book.objects.all()
    return render(request,'Library.html',{'book':book,'user':user})

def uploadform(request):
    upload = BookCreate()
    print("hello")
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        print("hi")
        if upload.is_valid():
            upload.save()
            return redirect('library')
        else:
            return HttpResponse("Failed to Upload Book")
    else:
        return render(request, 'Upload_form.html', {'upload': upload})

