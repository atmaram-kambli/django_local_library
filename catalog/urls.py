from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailsView.as_view(), name='book-detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
