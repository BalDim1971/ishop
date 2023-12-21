"""
URL configuration для приложения catalog.

"""

from django.conf.urls.static import static
from django.urls import path
from catalog.views import contact, ProductListView, ProductDetailView
from catalog.apps import CatalogConfig
from config import settings


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/info/', ProductDetailView.as_view(), name='info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
