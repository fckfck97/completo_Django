from django.db import models
from base.models import Modelo
from django.urls import reverse


#creando la tabla general de la paciente de obstetricia
class Paciente_obstetricia(Modelo):
	cedula = models.CharField(max_length=9,unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	edad = models.IntegerField()
	direccion = models.CharField(max_length=100)
	fecha = models.CharField(max_length=50)
	telefono = models.CharField(max_length=11)
	
	class Meta:
		ordering = ["-cedula"]
	def __str__(self):
		return self.cedula
	def get_absolute_url(self):
		return reverse('obstetricia:nuevo_paciente')

class Examen_fisico(Modelo):
	id_examen_fisico = models.AutoField(primary_key=True)
	ci_paciente = models.ForeignKey(Paciente_obstetricia, on_delete=models.CASCADE)
	ta = models.CharField(max_length=20)
	fc = models.CharField(max_length=20)
	fr = models.CharField(max_length=20)
	cardio_pul = models.CharField(max_length=200)
	mamas = models.CharField(max_length=200)
	abdomen = models.CharField(max_length=200)
	feto = models.CharField(max_length=200)
	normoconfigurados = models.CharField(max_length=200)
	cuello_uterino = models.CharField(max_length=200)
	extremidades = models.CharField(max_length=200)
	neurologico = models.CharField(max_length=200)
	class Meta:
		ordering = ["-ci_paciente"]
	def __str__(self):
		return str(self.id_examen_fisico)
	def get_absolute_url(self):
		return reverse('obstetricia:examen_fisico')

#creando la tabla que es relacionada con la tabla principal de obstetricia para parto normal
class Parto(Modelo):
	id_historia_parto = models.AutoField(primary_key=True)
	ci_paciente = models.ForeignKey(Paciente_obstetricia, on_delete=models.CASCADE)
	motivo_consulta = models.CharField(max_length=100)
	presenta = models.CharField(max_length=100)
	diagnostico = models.CharField(max_length=200)
	controles = models.IntegerField()
	deseado = models.BooleanField(default=False)
	planificado = models.BooleanField(default=False)
	controlado = models.BooleanField(default=False)
	itu = models.BooleanField(default=False)
	laboratorio = models.TextField()
	
	class Meta:
		ordering = ["-ci_paciente"]

	def __str__(self):
		return str(self.id_historia_parto)
	def get_absolute_url(self):
		return reverse('obstetricia:parto_nuevo')

#creando la nota de parto del paciente que se haya realizado el registrode parto
class Nota(Modelo):
	id_historia_nota_parto = models.AutoField(primary_key=True)
	ci_paciente = models.ForeignKey(Paciente_obstetricia, on_delete=models.CASCADE)
	nota_uno = models.CharField(max_length=100)
	nota_dos = models.CharField(max_length=100)
	nota_tres = models.CharField(max_length=100)
	nota_cuatro = models.CharField(max_length=100)
	nota_cinco = models.CharField(max_length=100)
	nota_seis = models.CharField(max_length=100)
	nota_siete = models.CharField(max_length=100,null=True)
	nota_ocho = models.CharField(max_length=100,null=True)
	nota_nueve = models.CharField(max_length=100,null=True)
	nota_diez = models.CharField(max_length=100,null=True)
	diagnostico2 = models.CharField(max_length=100)

	class Meta:
		ordering = ["-ci_paciente"]

	def __str__(self):
		return str(self.id_historia_nota_parto)
	def get_absolute_url(self):
		return reverse('obstetricia:nota_parto')

#
class Orden_medica_parto(Modelo):
	id_orden_medica_parto = models.AutoField(primary_key=True)
	ci_paciente = models.ForeignKey(Paciente_obstetricia, on_delete=models.CASCADE)
	orden_uno = models.CharField(max_length=50)
	orden_dos = models.CharField(max_length=50)
	orden_tres = models.CharField(max_length=50)
	orden_cuatro = models.CharField(max_length=50)
	orden_cinco = models.CharField(max_length=50)
	orden_seis = models.CharField(max_length=50)
	orden_siete = models.CharField(max_length=50,null=True)
	orden_ocho = models.CharField(max_length=50,null=True)
	orden_nueve = models.CharField(max_length=50,null=True)
	orden_diez = models.CharField(max_length=50,null=True)

	class Meta:
		ordering = ["-ci_paciente"]

	def __str__(self):
		return str(self.id_orden_medica_parto)
	def get_absolute_url(self):
		return reverse('obstetricia:orden_medica_parto')

class Antecedentes(models.Model):
	id_antecedentes = models.AutoField(primary_key=True)
	ci_paciente = models.ForeignKey(Paciente_obstetricia, on_delete=models.CASCADE)
	fur = models.CharField(max_length=11)
	gestas = models.IntegerField()
	partos = models.IntegerField()
	cesareas = models.IntegerField()
	legrados = models.IntegerField()
	antemadre = models.CharField(max_length=100)
	antepadre = models.CharField(max_length=100)
	antehermanos = models.CharField(max_length=100)
	antehijos = models.CharField(max_length=100)
	patologias = models.CharField(max_length=100)
	alergias = models.CharField(max_length=100)
	transfusiones = models.CharField(max_length=100)
	intervenciones = models.CharField(max_length=100)
	menarquia = models.IntegerField()
	sexarquia = models.IntegerField()
	ciclomens = models.CharField(max_length=30)
	parejas = models.IntegerField()
	aco = models.BooleanField(default=False)
	citologia = models.BooleanField(default=False)
	its = models.BooleanField(default=False)
	diu = models.BooleanField(default=False)
	embarazo_ante = models.CharField(max_length=200)
	
	class Meta:
		ordering = ["-ci_paciente"]

	def __str__(self):
		return str(self.id_antecedentes)