from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Book, Author, Publisher
from .forms import PublisherForm

KHALTI_VERIFY_URL = "https://khalti.com/api/v2/epayment/"
KHALTI_SECRET_KEY = "django-insecure-po%m(^w__!8kw$hpolk7glgbk-u16hd*1-(bfc1b8!kk7#icer"
import requests

# Create your views here.
def RelationHome(request):
    """Display paginated book list with all book data."""
    # Order by primary key to ensure stable pagination (created_at not present on model)
    books_list = Book.objects.all().select_related('publisher').prefetch_related('authors').order_by('-id')
    
    # Search functionality
    query = request.GET.get('q', '')
    if query:
        books_list = books_list.filter(
            Q(title__icontains=query) |
            Q(isbn__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query) |
            Q(publisher__name__icontains=query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(books_list, 6)  # 6 books per page
    page = request.GET.get('page')
    
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    
    context = {
        'books': books,
        'query': query,
        'total_books': paginator.count,
    }
    return render(request, 'Relation/booklist.html', context)

def RelationDetail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'Relation/bookdetails.html', {'book': book})

def book_detail(request, pk):
    """Show detailed view for a single book."""
    qs = Book.objects.select_related('publisher').prefetch_related('authors')
    book = get_object_or_404(qs, pk=pk)
    return render(request, 'Relation/book_detail.html', {'book': book})

def addpublisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relation:home')
    else:
        form = PublisherForm()
    return render(request, 'Relation/addPublisher.html', {'form': form})

@csrf_exempt
def verify_khalti_payment(request):
    if request.method == "POST":
        try:
            payload =json.loads(request.body)

            response = requests.post(
                KHALTI_VERIFY_URL,
                json={
                    'token': payload.get("token"),
                    'amount':payload.get("amount")
                },
                headers={
                    'Authorization':f'Bearer{KHALTI_SECRET_KEY}',
                    'Content-Type':'application/json'
                }
            )
            verification_data = response.json()
            if response.status_code == 200 and verification_data.get('status') == 'success':
                return JsonResponse({"success":True})
            else:
                return JsonResponse({"success":False},status=400)
        except Exception as e:
            return JsonResponse({"success":False,"error":str(e)},status=400)
    return JsonResponse({"success":False},status=400)