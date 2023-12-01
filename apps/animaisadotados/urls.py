from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'animaisadotado'

router = routers.DefaultRouter()
router.register('', views.AnimaisadotadoViewSet, basename='animaisadotados')

urlpatterns = [
    path('', include(router.urls) )
]