from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portrait/', views.portraitDetail, name='portrait'),
    path('lifestyle/', views.lifestyleDetail, name='lifestyle')
]
