# Generated by Django 4.1.2 on 2022-10-30 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0008_fotosdos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carpeta_uno',
            new_name='Convenciones',
        ),
        migrations.DeleteModel(
            name='Fotosdos',
        ),
    ]
