from django.conf.urls import url, include
from django.views.generic import ListView
from blog.models import BlogPost

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=BlogPost.objects.all().order_by("-date")[:10], template_name='blog/blog.html')),
]
