# Generated by Django 5.2 on 2025-05-26 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_notification_utilisateur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='id_plat',
        ),
        migrations.RemoveField(
            model_name='historique',
            name='id_ingredient',
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]
