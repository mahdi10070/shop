from django.urls import path
from . import views

app_name = 'carts'
urlpatterns = [
    path('cart', views.ShowCartView.as_view(), name='cart'),
    path('del_cart/<str:id>', views.RemoveItemCartView.as_view(), name='del_cart'),
    path('add_cart/<int:id>', views.AddCartSessionView.as_view(), name='add_cart'),
]
