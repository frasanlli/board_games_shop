from django.shortcuts import render
from .models import Post

# Create your views here.
def blog (request):

    posts = Post.objects.all()
    return render(request, "blog_app/blog.html", {"posts": posts})