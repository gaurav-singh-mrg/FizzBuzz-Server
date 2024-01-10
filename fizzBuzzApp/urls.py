"""
URL configuration for fizzBuzzApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import fizz_buzz, statistics, schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fizzbuzz/<int:int1>/<int:int2>/<int:limit>/<str:str1>/<str:str2>',  fizz_buzz, name='fizz_buzz'),
    path('statistics/', statistics, name='statistics'),
    path('docs/', schema_view),

]
