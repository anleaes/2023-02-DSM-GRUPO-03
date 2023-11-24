from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'especie'

router = routers.DefaultRouter()
router.register('especie', views.EspecieViewSet, basename='especie')

urlpatterns = [
    path('', include(router.urls) )
]