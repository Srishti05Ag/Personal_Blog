from django.shortcuts import render

from .models import Publication

def allpub(request):
    pubs = Publication.objects
    return render(request, 'blog/allpub.html', {'pubs':pubs})

