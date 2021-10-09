from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Blog

def home(request):
    return render(request, 'blog/home.html')

def englishpoem(request):
    blogs = Blog.objects
    return render(request, 'blog/englishpoem.html', {'blogs':blogs})

def blogdetail(request, poem_id):
    details = get_object_or_404(Blog, pk=poem_id)
    return render(request, 'blog/blogdetail.html', {'detaildict':details})

def like_func(request, poem_id):    
    if request.method == "POST":
        like_blog = get_object_or_404(Blog, pk=poem_id)
        like_blog.like_poem +=1
        like_blog.save()
        return redirect('/blog/' + str(like_blog.id))
