from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, ListView, View
from .models import Product, Category
from accounts.models import Information
from custom_mixing.customize_mixing import UserLoginMixin


# Create your views here.
class ProductDetailView(UserLoginMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    paginate_by = 3
    context_object_name = 'products'

class CategoryListView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk)
        products = category.product.all()
        return render(request, 'products/product_list.html', {'products': products})


class ProductLikeListView(UserLoginMixin, View):
    def get(self, request):
        if Information.objects.filter(user = request.user).exists():
            product_like = Information.objects.get(user = request.user)
            products = Product.objects.filter(information = product_like)
            if products:
                return render(request, 'products/List_of_interests.html', context = {'products': products})
            return render(request, 'products/List_of_interests.html', context = {})
        return render(request, 'products/List_of_interests.html', context={})

class RemoveProductLikeView(UserLoginMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        product_like = Information.objects.get(user = request.user)
        product_like.like_product.remove(product)
        return redirect('products:product_like')


class AddProductLikeView(UserLoginMixin, View):
    def get(self, request, id):
        product = Product.objects.get(id = id)
        like = Information.objects.get(user=request.user)
        like.like_product.add(product)
        like.save()
        url = request.GET.get('next')
        if url:
            return redirect(url)
        return redirect('products:product_list')

class SearchProductView(UserLoginMixin, View):
    def get(self, request):
        search = request.GET.get('q')
        products = Product.objects.filter(title__icontains=search)
        return render(request, 'products/product_list.html', {'products': products})