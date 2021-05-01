from django.shortcuts import render, get_object_or_404

from .models import Blog

def home(request):
    return render(request, 'blog/home.html')

def blogdetail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'detaildict':details})

def englishpoem(request):
    blogs = Blog.objects
    return render(request, 'blog/englishpoem.html', {'blogs':blogs})


