from django.urls import path
from . import views


urlpatterns = [
    path('englishpoem/',views.englishpoem, name='englishpoem'),
    path('<int:poem_id>/', views.blogdetail, name='blogdetail'),
    path('<int:poem_id>/like_func', views.like_func, name='like_func'),
]  
