from django.shortcuts import render, get_object_or_404, redirect

from .models import HindiBlog

def hindipoem(request):
    hindiblogs = HindiBlog.objects
    return render(request, 'hindiblog/hindipoem.html', {'hindiblogs':hindiblogs})

def hindiblogdetail(request, hindi_blog_id):
    details = get_object_or_404(HindiBlog, pk=hindi_blog_id)
    return render(request, 'hindiblog/hindiblogdetail.html', {'hindidict':details})

def vote_func(request, hindi_blog_id):
    if request.method == "POST":
        like_hindi = get_object_or_404(HindiBlog, pk=hindi_blog_id)
        like_hindi.vote +=1
        like_hindi.save()
        return redirect('/hindiblog/' + str(like_hindi.id))