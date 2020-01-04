from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Adress, AdressToUser, Cat, Coordonnees


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields =('__all__')




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

        # adress = Adress.objects.create(**validated_data)
        # for adress in adress:
        #     AdressToUser.create(user_id=User.created.id, adress=Adress.created.id )
        
        return user


class AdressToUserSerializer(serializers.ModelSerializer):
    
    user_id = UserSerializer(many=False)
    adress = AdressSerializer(many=False)
    class Meta:
        model = AdressToUser
        fields = ('id', 'user_id', 'adress')
        
        # authentication_classes = (TokenAuthentication,)
        # permission_classes = (IsAuthenticated,)

    def create(self, validated_data):
        adress_data = validated_data.pop('adress')
        user_data = validated_data.pop('user')
        AdressToUser.objects.create(user_id=user_data.id, adress=adress_data)
        return AdressToUser
        