from django.shortcuts import render
from .models import Post, Category

# Create your views here.
def blog (request):

    posts = Post.objects.all()
    categories = Category.objects.all()

    return render(request, "blog_app/blog.html", {"posts": posts, "categories": categories})


def category_filter (request, category_id):

    category = Category.objects.get(id = category_id)
    posts = Post.objects.filter(categories = category)
    categories = Category.objects.all()

    return render(request, "blog_app/category.html",
                  {"category": category, "posts": posts, "categories": categories})