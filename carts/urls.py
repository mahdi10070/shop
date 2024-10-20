from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('cart', views.CartView.as_view(), name='cart'),
    path('del_cart/<int:id>', views.DeleteItemCartView.as_view(), name='del_cart'),
    path('add_cart/<int:id>', views.AddToCartView.as_view(), name='add_cart'),
]