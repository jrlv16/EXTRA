from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
                            UserSerializer, 
                            AdressToUserSerializer, 
                            AdressSerializer,
                            CatSerializer, 
                        )
from .models import AdressToUser, Adress, Coordonnees, Cat

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)

          
    
class AdressToUserViewSet(viewsets.ModelViewSet):
    queryset = AdressToUser.objects.all().select_related('user', 'adress')
    serializer_class = AdressToUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)


class AdressViewSet(viewsets.ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AdressSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =(AllowAny,)