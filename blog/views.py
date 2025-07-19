
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def allpost(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

def detail(request, blog_id):
    detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'details.html', {'post': detail})



