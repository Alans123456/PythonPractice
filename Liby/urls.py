from django.urls import path
from . import views
from library.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL,DEBUG, STATIC_ROOT


urlpatterns = [
    path('library', views.LibraryHome, name='library'),
    path('uploadbook', views.uploadform, name='uploadbook'),
    path('update/<int:book_id>/', views.update_book, name='update_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('email', views.send_template_email, name='send_email'),
]

if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
