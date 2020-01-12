from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Adress, AdressToUser, Cat, Coordonnees


class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = ('id', 'numero', 'adress', 'code_postal', 'ville')


class CatSerializer(serializers.ModelSerializer):
    
    # user_id = UserSerializer()

    class Meta:
        model = Cat
        fields = ('id', 'user_id_id', 'cat')

    # def create(self, validated_data):
    #     user_data = validated_data.pop(user_id)
    #     cat = Cat.object.create(**validated_data)
    #     User.objects.create(**user_data)



class UserSerializer(serializers.ModelSerializer):
    cat = CatSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'cat')
        # permet de cacher le password à l'affichage du user
        extra_kwargs = {'password': {'write_only': True, 'required':True}}
        # permet de hasher le password avant enregistrement sinon en clair
    
    def create(self, validated_data):
        cat_data = validated_data.pop('cat')
        user = User.objects.create_user(**validated_data)
        Token.objects.get_or_create(user=user)
        Cat.objects.create(user_id_id=user.id, **cat_data)
        return user



class AdressToUserSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    adress = AdressSerializer()
    
    class Meta:
        model = AdressToUser
        fields = ('user', 'adress')
