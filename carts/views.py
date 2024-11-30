from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from accounts.models import Wallet
from products.models import Product
from custom_mixing.customize_mixing import UserLoginMixin
from .session import Cart

# Create your views here.

class CartView(UserLoginMixin, TemplateView):
    template_name = 'carts/cart.html'


class AddCartSessionView(UserLoginMixin, View):
    def post(self, request, id):
        product = Product.objects.get(id = id)
        print(f"in to add kardane ke {product.id}")
        count = request.POST.get('quantity-input')
        cart = Cart(request)
        cart.add_cart(product, count)
        print(count)
        return redirect('carts:cart')

class ShowCartView(UserLoginMixin, View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'carts/cart.html', {'cart': cart})

class RemoveItemCartView(UserLoginMixin, View):
    def get(self, request, id):
        cart = Cart(request)
        cart.remove_cart(id)
        return redirect('carts:cart')
