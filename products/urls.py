from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product_detail/<str:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:pk>', views.CategoryListView.as_view(), name='category'),
    path('product_list', views.ProductListView.as_view(), name='product_list'),
]