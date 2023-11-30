from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'adocao'

router = routers.DefaultRouter()
router.register('', views.OrderViewSet, basename='adocaos')

urlpatterns = [
    path('', include(router.urls) )
]