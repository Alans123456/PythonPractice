from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Book, Author, Publisher

# Create your views here.
def RelationHome(request):
    """Display paginated book list with all book data."""
    books_list = Book.objects.all().select_related('publisher').prefetch_related('authors')
    
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
