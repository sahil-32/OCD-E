"""ocde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views
from mainapp import views as mainapp_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compiler/', mainapp_views.compiler, name='compiler'),
    path('output/', mainapp_views.output, name='output'),
    path('reset/', mainapp_views.reset, name='reset'),
    path('register/',user_views.register, name='register'),
    path('upload/',user_views.post, name='upload'),
    path('viewfile/<int:pk>',user_views.delete, name='delete'),
    path('edit/<int:pk>',mainapp_views.edit, name='edit'),
    path('viewfile/',user_views.get, name='viewfile'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('',mainapp_views.home, name='homepage'),
]
