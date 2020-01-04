from django.contrib import admin

from .models import Metier, Corporation, Etablissement, AdressToEtablissement

admin.site.register(Metier)
admin.site.register(Corporation)
admin.site.register(Etablissement)
admin.site.register(AdressToEtablissement)