from django.shortcuts import render, get_object_or_404
from .models import Post, Author

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author).order_by("-published_date")
    return render(request, "blog/posts_by_author.html", {"author": author, "posts": posts})