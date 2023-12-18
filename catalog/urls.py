"""
URL configuration для приложения catalog.

"""

from django.urls import path
from catalog.views import index, contact
from django.contrib import admin
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('product/', contact, name='product'),
    path('admin/', admin.site.urls)
]
