from django.db import models
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from EXTRA.models import Adress



class Corporation(models.Model):
    ''' 
    Définition des corporations pour les applis futures
    '''
    nom = models.CharField("Corporation", max_length=50)

    def __str__(self):
        return self.nom


class Metier(models.Model):
    ''' 
    Définition des métiers exercés par les extras
    '''
    nom = models.CharField("Métier", max_length=50)
    taux_horaire_normal = models.DecimalField("taux horaire", max_digits=5, decimal_places=2)
    taux_horaire_special = models.DecimalField("taux horaire spécial", max_digits=5, decimal_places=2)
    categorie = models.ForeignKey("Corporation", verbose_name="Corporation", on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Etablissement(models.Model):
    enseigne = models.CharField("Enseigne", max_length=100)
    corporation = models.ForeignKey("Corporation", verbose_name="Corporation", on_delete=models.SET_NULL, null=True, default="1")
    gerant = models.ForeignKey(User, verbose_name="Gérant", related_name="gerant", on_delete=models.SET_NULL, null=True)
    proprio = models.ForeignKey(User, verbose_name="Propriétaire", related_name="proprio",on_delete=models.CASCADE)
    valide = models.BooleanField("Validé", default=False)

    @classmethod
    def get_adress(cls, etab_id):
        adress = get_object_or_404(AdressToEtablissement, id=etab_id)
        return adress
    
    
    def __str__(self):
        d = self.corporation.nom + "  " + self.enseigne 
        return d

class AdressToEtablissement(models.Model):
    etablissement = models.ForeignKey(Etablissement, verbose_name="Etablissement", on_delete=models.CASCADE)
    adress = models.ForeignKey(Adress, verbose_name="Adresse", on_delete=models.CASCADE)
