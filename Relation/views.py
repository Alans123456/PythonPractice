from django.shortcuts import render

# Create your views here.
def RelationHome(request):
    return render(request,'Relation/booklist.html')
