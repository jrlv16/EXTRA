# Generated by Django 3.0 on 2019-12-27 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('METIER', '0002_etablissement_corporation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etablissement',
            name='adress',
        ),
    ]
