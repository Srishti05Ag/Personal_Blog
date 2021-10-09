from django.urls import path
from . import views


urlpatterns = [
    path('hindipoem/',views.hindipoem, name='hindipoem'),
    path('<int:hindi_blog_id>/', views.hindiblogdetail, name='hindiblogdetail'),
    path('<int:hindi_blog_id>/vote_func', views.vote_func, name='vote_func'),
]  

