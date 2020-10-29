"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),  
    path('adminhome/', views.adminhome, name="adminhome"),  
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('userhome/', views.userhome, name="userhome"),  
    path('userlogout/', views.userlogout, name="userlogout"),
    path('uploaddataset/', views.uploaddataset, name="uploaddataset"), 
    path('xlupload/', views.xlupload, name="xlupload"), 
    path('viewdataset/', views.viewdataset, name="viewdataset"), 
    path('signup/', views.signupaction, name="signup"), 
    path('userlogin/', views.userlogin, name="userlogin"), 
    path('getcalories/', views.getcalories, name="getcalories"), 
    
    
]
