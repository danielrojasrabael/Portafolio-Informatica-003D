# Generated by Django 4.1 on 2022-08-27 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SSAP', '0004_administradores_xd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administradores',
            name='xd',
        ),
    ]
