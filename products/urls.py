from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product_detail/<str:slug>', views.ProductDetailView.as_view(), name='product_detail'),
    path('product_like', views.ProductLikeListView.as_view(), name='product_like'),
    path('remove/product_like/<int:id>', views.RemoveProductLikeView.as_view(), name='remove_product_like'),
    path('add/product_like/<int:id>', views.AddProductLikeView.as_view(), name='add_product_like'),
    path('category/<int:pk>', views.CategoryListView.as_view(), name='category'),
    path('product_list', views.ProductListView.as_view(), name='product_list'),
    path('search', views.SearchProductView.as_view(), name='search'),
]
