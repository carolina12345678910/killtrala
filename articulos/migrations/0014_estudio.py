# Generated by Django 4.1.1 on 2022-11-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0013_alter_entrada_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
            ],
        ),
    ]
