from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from accounts.models import Wallet
from products.models import Product
from custom_mixing.customize_mixing import UserLoginMixin

# Create your views here.

class CartView(UserLoginMixin, TemplateView):
    template_name = 'carts/cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class AddToCartView(UserLoginMixin, View):
    def get(self, request, id):
        item = Product.objects.get(id=id)
        wallet = Wallet.objects.get(user = request.user)
        wallet.product.add(item)
        wallet.save()
        url = request.GET.get('next')
        if url is not None:
            return redirect(url)
        return redirect('carts:cart')

    def post(self, request, id):
        product = Product.objects.get(id = id)
        Wallet.objects.create(user = request.user, product = product)
        url = request.GET.get('next')
        if url is not None:
            return redirect(url)
        return redirect('carts:cart')


class DeleteItemCartView(UserLoginMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id=id)
        wallet = Wallet.objects.get(user = request.user)
        wallet.product.remove(product)
        url = request.GET.get('next')
        if url is not None:
            return redirect(url)
        return redirect('carts:cart')

