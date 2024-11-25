from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Blog


# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 1



class BlogDetailView(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        return render(request, 'blog/blog_detail.html', context= {'blog': blog})