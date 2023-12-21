"""
URL configuration для приложения blog.

"""

from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView


app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    # path('edit/<int:pk>', ..., name='edit'),
    # path('delete/<int:pk>', ..., name='delete'),
]
