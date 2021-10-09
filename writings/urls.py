from django.urls import path
from . import views


urlpatterns = [
    path('writings/',views.writings, name='writings'),
    path('<int:blog_id>/', views.writingsdetail, name='writingsdetail'),
    path('<int:blog_id>/liked', views.liked, name='liked'),
]  

