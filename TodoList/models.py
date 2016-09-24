from django.db import models
from django.contrib.auth.models import User

class Cliente(User):
	titulo = (
	('Sr', 'Sr'),
    ('Srita', 'Srita'),
    ('Sra', 'Sra'),
    ('Don', 'Don'),
    ('Ingeniero', 'Ingeniero'),
    ('Doctor', 'Doctor'))
	tratamiento = models.CharField(max_length=15,choices=titulo,default=None)

	def __str__(self):
		return '{0} - {1}'.format(self.username, self.tratamiento)

class Categoria(models.Model):
	nombre = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre

class Nota(models.Model):
	usuario = models.ForeignKey(Cliente)
	nota = models.CharField(max_length=50)
	categoria = models.ForeignKey(Categoria)
	lista = (
	('Urgente', 'Urgente'),
    ('Normal', 'Normal'),
    ('Relajao', 'Rejalao'),
	('Pendiente', 'Pendiente'),
   )
	prioridad = models.CharField(max_length=10,choices=lista,default=None)
	completada = models.BooleanField(default=False)

	def __str__(self):
		return self.nota