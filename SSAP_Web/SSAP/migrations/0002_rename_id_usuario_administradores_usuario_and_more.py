# Generated by Django 4.1 on 2022-08-27 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SSAP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administradores',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='profesionales',
            old_name='id_usuario',
            new_name='usuario',
        ),
    ]
