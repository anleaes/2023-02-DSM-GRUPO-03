from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'especies'

router = routers.DefaultRouter()
router.register('especie', views.EspecieViewSet, basename='especie')

urlpatterns = [
    path('', include(router.urls) )
]