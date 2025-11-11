from django.shortcuts import render,redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages

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

def update_book(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('library')
    book_form = BookCreate(request.POST or None, request.FILES or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('library')
    return render(request, 'Upload_form.html', {'upload': book_form, 'book_id': book_id})

def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('library')
    book_sel.delete()
    return redirect('library')
    
def send_template_email(request):
    if request.method == 'POST':
        from_email = "alansshrestha62@gmail.com"
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        try:
            send_mail(subject, body, from_email, [to_email])
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, f'Error sending email: {str(e)}')
        return redirect('library')
    else:
        return redirect('library')

