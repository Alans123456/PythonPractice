from django.shortcuts import render

# Create your views here.
def LibraryHome(request):
    return render(request,'Library.html')

