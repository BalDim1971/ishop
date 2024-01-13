"""
URL configuration для приложения catalog.

"""

from django.conf.urls.static import static
from django.urls import path
from catalog.views import contact, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryCreateView, CategoryListView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView
from catalog.apps import CatalogConfig
from config import settings


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category_info/<int:pk>', CategoryDetailView.as_view(), name='category_info'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('contacts/', contact, name='contacts'),
    path('info/<int:pk>', ProductDetailView.as_view(), name='info'),
    path('create', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
