# Generated by Django 5.2 on 2025-05-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_commande_plat_ingredient_historique_commandeplat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
