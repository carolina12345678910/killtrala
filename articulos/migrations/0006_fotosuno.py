# Generated by Django 4.1.2 on 2022-10-30 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0005_alter_estilouno_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotosuno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('foto', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
