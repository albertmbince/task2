"""project5 URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from App import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('user_login/',views.user_login,name='login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('add/',views.add_book,name='add'),
    path('list/',views.view_book,name='list'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('add_book/',views.add_book,name='add_book'),
    path('list/',views.view_book,name='list'),
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)