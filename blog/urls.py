from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.add, name='result'),
    path('contact/', views.contact, name='contact'),
]
