
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView
from .views import fizz_buzz, statistics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fizzbuzz/<int:int1>/<int:int2>/<int:limit>/<str:str1>/<str:str2>', fizz_buzz, name='fizz_buzz'),
    path('statistics/', statistics, name='statistics'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

]
