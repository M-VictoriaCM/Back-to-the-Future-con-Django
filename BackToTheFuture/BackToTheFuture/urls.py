"""BackToTheFuture URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import pagina_inicio, trilogia, personajes, miscelaneas, contacto, vaf1

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', pagina_inicio, name = 'pagina_inicio'),
    path('trilogia/', trilogia, name = 'trilogia'), 
    path('trilogia/', trilogia, name = 'trilogia'), 
    path('personajes/', personajes, name = 'personajes'), 
    path('miscelaneas/', miscelaneas, name = 'miscelaneas'),
    path('contacto/', contacto, name = 'contacto'),  
    path('vaf1/', vaf1 , name="vaf1"),

]
