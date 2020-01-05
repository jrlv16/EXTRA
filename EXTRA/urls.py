from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import UserViewSet, AdressToUserViewSet, AdressViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('adress', AdressViewSet)
router.register('adresstouser', AdressToUserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
