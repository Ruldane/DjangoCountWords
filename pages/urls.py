from django.urls import path, include
# '.' means, it's in our directory
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('count/', views.count, name='count'),
    path('about/', views.about, name='about'),
    ]