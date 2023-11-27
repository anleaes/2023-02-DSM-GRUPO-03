from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ongs'

router = routers.DefaultRouter()
router.register('ong', views.OngViewSet, basename='ong')

urlpatterns = [
    path('', include(router.urls) )
]