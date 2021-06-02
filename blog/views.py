from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import HttpResponse

from .models import Blog

def home(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        data={
            'first_name':first_name,
            'last_name':last_name,
            'email_address':email_address,
            'message':message
        }
        message = '''
        New message: {}

        From: {}

        First Name: {}

        Last Name: {}
        '''.format(data['message'], data['email'], data['first_name'], data['last_name'])
        
        send_mail(data['first_name'], data['last_name'], message, '', ['sweetsrishtiagrawal09@gmail.com'])
        return HttpResponse('Thanks !!! Your valuable response has been received. We will be in touch at the earliest')

    return render(request, 'blog/home.html')

def blogdetail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blogdetail.html', {'detaildict':details})

def englishpoem(request):
    blogs = Blog.objects
    return render(request, 'blog/englishpoem.html', {'blogs':blogs})


# def contact(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email_address = request.POST.get('email_address')
#         message = request.POST.get('message')

#         data={
#             'first_name':first_name,
#             'last_name':last_name,
#             'email_address':email_address,
#             'message':message
#         }
#         message = '''
#         New message: {}

#         From: {}

#         First Name: {}

#         Last Name: {}
#         '''.format(data['message'], data['email'], data['first_name'], data['last_name'])
        
#         send_mail(data['first_name'], data['last_name'], message, '', ['sweetsrishtiagrawal09@gmail.com'])
#         return HttpResponse('Thanks !!! Your valuable response has been received. We will be in touch at the earliest')      
#     return render(request, "blog/home.html", {})