"""
URL configuration для приложения catalog.

"""

from django.urls import path
from catalog.views import index, contact

app_name = 'catalog'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
