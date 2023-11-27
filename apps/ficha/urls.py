from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'ficha'

router = routers.DefaultRouter()
router.register('ficha', views.FichaViewSet, basename='ficha')

urlpatterns = [
    path('', include(router.urls) )
]
