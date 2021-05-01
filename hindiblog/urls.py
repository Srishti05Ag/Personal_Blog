from django.urls import path
from . import views


urlpatterns = [
    path('hindipoem/<int:blog_id>/', views.hindiblogdetail, name='hindiblogdetail'),
    path('hindipoem/',views.hindipoem, name='hindipoem'),
]  

