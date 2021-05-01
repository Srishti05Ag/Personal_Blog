from django.shortcuts import render, get_object_or_404

from .models import HindiBlog

def hindipoem(request):
    hindiblogs = HindiBlog.objects
    return render(request, 'hindiblog/hindipoem.html', {'hindiblogs':hindiblogs})

def hindiblogdetail(request, blog_id):
    details = get_object_or_404(HindiBlog, pk=blog_id)
    return render(request, 'hindiblog/hindiblogdetail.html', {'hindidict':details})

