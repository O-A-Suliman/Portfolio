from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('certificates1/', views.certificates1, name='certificates1'),
    path('certificates2/', views.certificates2, name='certificates2'),
]
