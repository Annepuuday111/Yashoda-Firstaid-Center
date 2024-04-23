from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('login/', views.login, name='login'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('booking/', views.booking, name='booking'),
    path('admindashboard/', views.admindashboard, name='admindashboard'),
]
