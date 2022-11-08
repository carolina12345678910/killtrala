from django.db import models

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=60)
    foto = models.ImageField(upload_to='imagenes/')

    def __str__(self):
    	return self.titulo


class Tinturas(models.Model):
	nombre = models.TextField()
	imagen = models.ImageField(upload_to = 'imagenes/')

	def __str__(self):
		return self.nombre

class Diseños_varios(models.Model):
	nombre = models.CharField(max_length=60)
	fotografia = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.nombre

class Convenciones(models.Model):
	nombre = models.CharField(max_length=60)
	imagenes = models.ImageField(upload_to='imagenes/')


	def __str__(self):
		return self.nombre


class Estudio(models.Model):
	nombre = models.CharField(max_length=60)
	imagen = models.ImageField(upload_to='imagenes/')

	def __str__(self):
		return self.nombre


class Tatuadores(models.Model):
	nombre = models.CharField(max_length=60)
	foto = models.ImageField(upload_to='imagenes/')
	informacion = models.TextField(max_length=300)

	def __str__(self):
		return self.nombre


class Adicional(models.Model):
	titulo = models.CharField(max_length=60)
	informacion = models.TextField(max_length=300)

	def __str__(self):
		return self.titulo


