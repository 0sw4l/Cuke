__author__ = 'osw4l'
from django.forms import ModelForm
from .models import Nota, Categoria, Cliente
from django import forms
from django.contrib.auth.forms import UserCreationForm

class NotaForm(ModelForm):
    class Meta:
        model = Nota
        exclude = ['usuario', 'completada']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = (
        	"last_login",
        	"groups",
        	"user_permissions",
        	"is_staff",
        	"is_active",
        	"is_superuser",
        	"date_joined",)

class CrearClienteForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ['username','first_name','tratamiento']

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
