from django.db import models

# Create your models here.
class Modelo(models.Model):
	fecha = models.CharField(max_length=50)
	medico_nombre = models.CharField(max_length=50)
	medico_apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=10)
	rango = models.CharField(max_length=30)
	telefono = models.CharField(max_length=30)

	class Meta:
		abstract=True