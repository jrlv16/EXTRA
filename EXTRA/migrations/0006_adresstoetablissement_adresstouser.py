# Generated by Django 3.0 on 2019-12-27 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('METIER', '0003_remove_etablissement_adress'),
        ('EXTRA', '0005_remove_adress_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdressToUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EXTRA.Adress', verbose_name='Adresse')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='AdressToEtablissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EXTRA.Adress', verbose_name='Adresse')),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='METIER.Etablissement', verbose_name='Etbalissement')),
            ],
        ),
    ]
