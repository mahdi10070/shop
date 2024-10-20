from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView, View
from .models import Product, Category
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
