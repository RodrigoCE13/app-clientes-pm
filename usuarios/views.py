from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.models import User
from .forms import ExtendedUserCreationForm
from django.contrib.auth.forms import UserChangeForm
from appclientes.decorators import admin_only

# Create your views here.

@login_required
@admin_only
#listar usuarios
def usuarios(request):
    queryset = request.GET.get("buscar")
    usuarios = User.objects.filter(is_active=True)
    
    if queryset:
        usuarios = usuarios.filter(
            Q(first_name__icontains=queryset) |
            Q(email__icontains=queryset)
        ).distinct()
    
    usuarios = usuarios.exclude(username='admin')
    
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@login_required
@admin_only
#editar usuario
def usuario_detail(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'GET':
        form = UserChangeForm(instance=usuario)
        return render(request, 'usuario-detail.html', {'usuario': usuario, 'form': form})
    else:
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        return render(request, 'usuario-detail.html', {'usuario': usuario, 'form': form, 'error': 'Error al editar usuario'})

@login_required
@admin_only
#desactivar usuario
def desactivar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    
    # Verificar que el usuario no sea el superusuario 'admin'
    if usuario.username == 'admin':
        # No se puede desactivar el superusuario
        return redirect('usuarios')
    
    # Desactivar al usuario
    usuario.is_active = False
    usuario.save()
    
    return redirect('usuarios')
@login_required
@admin_only
#activar usuario
def activar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.is_active = True
    usuario.save()
    return redirect('usuarios')


@login_required
@admin_only
#eliminar usuario
def usuario_delete(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        if usuario.username != 'admin':
            usuario.delete()
    return redirect('usuarios')

@login_required
@admin_only
#registrar_usuarios
def registrar_usuarios(request):
    if request.method == 'GET':
        return render(request, 'create-usuario.html', {'form': ExtendedUserCreationForm()})
    else:
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                if 'is_admin' in request.POST and request.POST['is_admin'] == 'on':
                    user.is_staff = True  # Asignar el rol de administrador al usuario
                user.save()
                return redirect('usuarios')
            except IntegrityError:
                return render(request, 'create-usuario.html', {
                    'form': form,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'create-usuario.html', {
            'form': form,
            'error': 'Las contraseñas no coinciden'
        })

from django.contrib.auth.models import User


