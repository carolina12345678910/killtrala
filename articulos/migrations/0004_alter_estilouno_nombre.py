# Generated by Django 4.1.2 on 2022-10-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0003_alter_estilouno_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estilouno',
            name='nombre',
            field=models.CharField(max_length=400),
        ),
    ]