# Generated by Django 3.0 on 2020-01-13 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EXTRA', '0011_auto_20200109_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordonnees',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coordonnees', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur'),
        ),
    ]
