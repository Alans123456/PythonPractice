from django.urls import path
from . import views
from library.settings import MEDIA_URL, MEDIA_ROOT, STATIC_URL,DEBUG, STATIC_ROOT


urlpatterns = [
    path('library', views.LibraryHome, name='library'),
    path('uploadbook', views.uploadform, name='uploadbook'),
]

if DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
