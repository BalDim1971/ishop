"""
URL configuration для приложения blog.

"""

from django.urls import path

from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('create/', ..., name='list'),
    path('view/<int:pk>', ..., name='view'),
    path('edit/<int:pk>', ..., name='edit'),
    path('delete/<int:pk>', ..., name='delete'),
]
