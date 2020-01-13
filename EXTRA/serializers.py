from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Adress, AdressToUser, Cat, Coordonnees

class CoordonneesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordonnees
        fields =['user_id_id', 'phone', 'phonefix']

class AdressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Adress
        fields = ('id', 'numero', 'adress', 'code_postal', 'ville')


class CatSerializer(serializers.ModelSerializer):
    
    # user_id = UserSerializer()

    class Meta:
        model = Cat
        fields = ('id', 'user_id_id', 'cat')

class AdressToUserSerializer(serializers.ModelSerializer):
    
    
    adress = AdressSerializer()
    
    class Meta:
        model = AdressToUser
        fields = ('adress',)

    def create(self, validated_data):
        user = self.request.user
        adress = Adress.objects.create(user_id_id=user.id, **validated_data)
        return adress


class UserSerializer(serializers.ModelSerializer):
    cat = CatSerializer()
    coordonnees = CoordonneesSerializer()
    # adress = AdressToUserSerializer()
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'cat', 'coordonnees')
        # permet de cacher le password à l'affichage du user
        extra_kwargs = {'password': {'write_only': True, 'required':True}}
        # permet de hasher le password avant enregistrement sinon en clair
        
    
    def create(self, validated_data):
        cat_data = validated_data.pop('cat')
        coord_data = validated_data.pop('coordonnees')  #1
        # adress_data = validated_data.pop('adress') #2
        user = User.objects.create_user(**validated_data)
        Token.objects.get_or_create(user=user)
        Cat.objects.create(user_id_id=user.id, **cat_data)
        Coordonnees.objects.create(user_id_id=user.id, **coord_data) #3
        # AdressToUser.objects.create(user_id=user.id, **adress_data) #4
        return user


class AdressToUserSerializer(serializers.ModelSerializer):
    
    
    adress = AdressSerializer()
    
    class Meta:
        model = AdressToUser
        fields = ('adress',)

    def create(self, validated_data):
        user = self.request.user
        adress = Adress.objects.create(user_id_id=user.id, **validated_data)
        return adress

