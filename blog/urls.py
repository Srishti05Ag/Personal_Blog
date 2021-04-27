from django.urls import path

from . import views

urlpatterns = [
    path('<int:blog_id>/', views.blogdetail, name='blogdetail'),
]  

