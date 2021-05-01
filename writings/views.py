from django.shortcuts import render, get_object_or_404

from .models import Writings

def writings(request):
    contents = Writings.objects
    return render(request, 'writings/writings.html', {'content':contents})

def writingsdetail(request, blog_id):
    details = get_object_or_404(Writings, pk=blog_id)
    return render(request, 'writings/writingsdetail.html', {'contentdict':details})


