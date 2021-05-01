from django.urls import path
from . import views


urlpatterns = [
    path('writings/<int:blog_id>/', views.writingsdetail, name='writingsdetail'),
    path('writings/',views.writings, name='writings'),
]  

