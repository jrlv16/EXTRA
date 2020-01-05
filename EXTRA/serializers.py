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
        
        return user


class AdressToUserSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(many=False)
    adress = AdressSerializer(many=False)
    
    class Meta:
        model = AdressToUser
        fields = ('user', 'adress')
        
        # authentication_classes = (TokenAuthentication,)
        # permission_classes = (IsAuthenticated,)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer(data=user_data)
        user.is_valid()
        user = user.save()

        adress_data = validated_data.pop('adress')
        adress = AdressSerializer(data=adress_data)
        adress.is_valid()
        adress = adress.save()

        print(user.id, adress.id)
        # {'user': user.id, 'adress_id': adress.id}
        AdressToUser.objects.create(**{'user': user.id, 'adress_id': adress.id})
        
        return AdressToUser



