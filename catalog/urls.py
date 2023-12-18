"""
URL configuration для приложения catalog.

"""

from django.conf.urls.static import static
from django.urls import path
from catalog.views import index, contact, info
from catalog.apps import CatalogConfig
from config import settings


app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>/catalog/info/', info, name='info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
