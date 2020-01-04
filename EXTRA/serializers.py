from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Adress, AdressToUser, Cat, Coordonnees


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        # permet de cacher le password à l'affichage du user
        extra_kwargs = {'password': {'write_only': True, 'required':True}}
        # permet de hasher le password avant enregistrement sinon en clair
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class AdressToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdressToUser
        fields = ('id', 'user_id', 'adress')
        # authentication_classes = (TokenAuthentication,)
        # permission_classes = (IsAuthenticated,)