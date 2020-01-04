from django.contrib import admin

from .models import (Cat, 
                    Coordonnees, 
                    Adress,
                    AdressToUser)

admin.site.register(Cat)
admin.site.register(Coordonnees)
admin.site.register(Adress)
admin.site.register(AdressToUser)
