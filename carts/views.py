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

    def post(self, request, id):
        product = Product.objects.get(id = id)
        count = request.POST.get('quantity-input')
        if Wallet.objects.filter(user = request.user).exists():
            print('inside')
            object = Wallet.objects.get(user = request.user)
            object.product.add(product)
            object.save()
        else:
            print('outside')
            object = Wallet.objects.create(user = request.user, count = count)
            object.product.add(product)
            object.count.add(int(count))
            object.save()
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

