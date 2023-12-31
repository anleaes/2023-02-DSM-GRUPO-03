"""adocaoapp URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adocaos/', include('adocaos.urls', namespace='adocaos')),
    path('animaisadotados/', include('animaisadotados.urls', namespace='animaisadotados')),
    path('animais/', include('animais.urls', namespace='animais')),
    path('veterinarios/', include('veterinarios.urls', namespace='veterinarios')),
    path('fichas/', include('fichas.urls', namespace='fichas')),
    path('especies/', include('especies.urls', namespace='especies')),
    path('ongs/', include('ongs.urls', namespace='ongs')),
    path('pessoas/', include('pessoas.urls', namespace='pessoas')),
    
]
