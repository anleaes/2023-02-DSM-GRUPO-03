from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'fichas'

router = routers.DefaultRouter()
router.register('', views.FichaViewSet, basename='ficha')

urlpatterns = [
    path('', include(router.urls) )
]
