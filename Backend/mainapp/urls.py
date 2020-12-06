from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('compiler/', views.compiler, name='compiler'),
    path('output/', views.output, name='output'),
]
