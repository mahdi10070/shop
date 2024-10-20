from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blogs', views.BlogListView.as_view(), name='blog_list'),
    path('blog-detial', views.BlogDetailView.as_view(), name='blog_detail'),
]