"""zipcopy2 URL Configuration

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
from django.urls import include, path
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from core.views import AddUser, PremiumJobList, OrderList
urlpatterns = [
    url(r'^auth/login/', obtain_jwt_token),
    url(r'^users/$', AddUser.as_view(), name='users'),
    url(r'^premium_jobs/$', PremiumJobList.as_view(), name='premium_jobs'),
    url(r'^orders/$', OrderList.as_view(), name='orders'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
