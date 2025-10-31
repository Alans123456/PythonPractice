from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def SignUpPage(request):
    error_message = None
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST['password']
        confirm_password = request.POST["confirm"]

        if password != confirm_password:
            error_message = "Passwords do not match."
        elif User.objects.filter(email=email).exists():
            error_message = "Email already exists."
        elif User.objects.filter(username=username).exists():
            error_message = "Username already exists."
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            return redirect('login')
    
    return render(request, "SignUp.html", {"error": error_message})
def LoginPage(request):
    error_message = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('library')
        else:
            error_message = "Invalid username or password."
    return render(request, "Login.html", {"error": error_message})

def LibraryPage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "Library.html")

