from django.urls import path
from . import views


urlpatterns = [
    path('englishpoem/<int:blog_id>/', views.blogdetail, name='blogdetail'),
    path('englishpoem/',views.englishpoem, name='englishpoem'),
]  

