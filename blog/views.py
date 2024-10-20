from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class BlogListView(View):
    def get(self, request):
        return render(request, 'blog/blog.html', context = {})


class BlogDetailView(View):
    def get(self, request, pk):
        return render(request, 'blog/blog-detail.html', context= {})