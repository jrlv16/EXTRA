from django.db import models
from django.contrib.auth.models import AbstractUser, User
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _



class Cat(models.Model):
    user_id = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name='cat')
    PROPRIETAIRE = 'PROPR'
    GERANT = 'GERAN'
    EXTRA = 'EXTRA'
    
    CAT_CHOICES = (
        (PROPRIETAIRE, 'Propriétaire'),
        (GERANT, 'Gérant'),
        (EXTRA, 'Extra'),
        )
    cat = models.CharField("categorie", 
                            max_length=5,
                            choices=CAT_CHOICES,
                            default="")

    def __str__(self):
        d = '%s %s %s' % (self.user_id.last_name, self.user_id.first_name, self.cat)
        return d 


class Coordonnees(models.Model):
    user_id = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name='coordonnees')
    phone = PhoneNumberField(_("Portable"), null=False, blank=False, unique=True)
    phonefix = PhoneNumberField(_("Tel Fixe"), null=True, blank=True)

    def __str__(self):
        d = '%s %s %s' % (self.user_id.last_name, self.user_id.first_name, self.phone)
        return d 


class Adress(models.Model):
    """
    Adresse utilisable pour les extras et les restaus
    """
    numero = models.PositiveIntegerField(_('numéro'), blank=True, null=True)
    adress = models.CharField(_('nom de la voie'), max_length=254, blank=False, null=False)
    code_postal = models.PositiveIntegerField(_('Code Postal'), blank=False, null=False)
    ville = models.CharField(_('Ville'), max_length=100, blank=False, null=False)
    

    def __str__(self):
        return '%s %s %s %s' % (self.numero, self.adress, self.code_postal, self.ville )    


class AdressToUser(models.Model):
    user = models.ForeignKey(User, verbose_name="Utilisateur", on_delete=models.CASCADE, related_name='users',)
    adress = models.ForeignKey(Adress, verbose_name="Adresse", on_delete=models.CASCADE, related_name='adresses')

    def __str__(self):
        return '%s %s' % (self.user_id, self.adress)
