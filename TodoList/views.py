from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import CategoriaForm, NotaForm, CrearClienteForm

def registrar(request):
    form = CrearClienteForm()
    if request.POST:
        form = CrearClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form,
        'button':'registrar',
        'add': True,
        'titulo' : 'Registro',
        'home':False,
        'button':'YAY ! Registrar'
    }
    return render(request, 'create.html', context)

def log_in(request):
    titulo = 'Cuke! - Todo List'
    context = {'titulo' : titulo , 'panel':False}
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                context = {'titulo' : titulo , 'msj':'El usuario ha sido desactivado :(','panel':True}
        else:
            context = {'titulo' : titulo ,'msj':'Usuario o Password incorrecta','panel':True}
    return render(request,'login.html', context)

@login_required
def home(request):
    user = request.user
    if user.is_staff:
        notas = Nota.objects.all()
        count = notas.count()
    else:
        notas = Nota.objects.filter(usuario=user).order_by('-id')
        count = notas.count()
    context = {
        'user':user,
        'titulo':'Mis CukeNotas',
        'notas':notas,
        'count' : count
    }
    return render(request,'to_do.html', context)

@login_required
def crear(request):
    form = NotaForm(instance=request.user)
    if request.POST:
        usuario = Nota(usuario=request.user.cliente)
        form = NotaForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario.save()
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'button':'Crear nota',
        'titulo' : 'nueva nota',
        'home':True,
        'button':'Crear Nota'
    }
    return render(request, 'create.html', context)

@login_required
def editar(request, pk):
    nota = Nota.objects.get(id=pk)
    form = NotaForm(instance=nota)
    if request.POST:
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
        'button':'Guardar cambios',
        'titulo':'editar',
        'home':True,
        'button':'Guardar'
    }
    return render(request, 'create.html', context)

@login_required
def borrar(request, pk):
    nota = Nota.objects.get(id=pk)
    nota.delete()
    return redirect('home')

@login_required
def cumplir(request, pk):
    tarea = Nota.objects.get(id=pk)
    tarea.completada=True
    tarea.save()
    return redirect('home')

@login_required
def nueva_categoria(request):
    if request.POST:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    context = {
        'form': form,
        'button':'crear categoria',
        'titulo' : 'crear categoria',
        'home':True,
        'button':'Crear Categoria'
    }
    return render(request, 'create.html', context)

@login_required
def log_out(request):
        logout(request)
        return redirect('login')
