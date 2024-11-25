from django.views.generic import TemplateView

from blog.models import Blog
from products.models import Product


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()[4:]
        context['products_old'] = Product.objects.all()[:5]
        context['blogs'] = Blog.objects.all()
        return context
