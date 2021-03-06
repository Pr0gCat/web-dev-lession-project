"""JsonGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('s', views.s, name='s'),
    path('s/<str:user_name>', views.s, name='s'),
    path('c', views.c, name='c'),
    path('d', views.d, name='d'),
    path('u/<str:user_name>', views.user_profile, name='user'),
    path('active',views.active,name='active'),
    path('pending',views.pending,name='pending'),
    path('completed',views.completed,name='completed'),
    path('cancelled',views.cancelled,name='cancelled'),
    path('acceptorders/<int:id>',views.acceptorders,name='acceptorders'),
    path('rejectorders/<int:id>',views.rejectorders,name='rejectorders'),
    path('done/<int:id>',views.done,name='done')
]
