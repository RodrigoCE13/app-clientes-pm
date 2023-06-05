from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required
#listar usuarios
def usuarios(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    usuarios = Usuario.objects.filter(estado=True)
    if queryset:
        usuarios=Usuario.objects.filter(
            Q(nombre__icontains= queryset)|
            Q(apellido__icontains=queryset)
        ).distinct()   
    usuarios=Usuario.objects.all()#en caso de quere mostrar solo los datos del usuario logeado ""Cliente.objects.filter(user=request.user)""
    return render(request, 'usuarios.html',{'usuarios':usuarios})

@login_required
#crear usuarios
def create_usuarios(request):
    if request.method == 'GET':
        return render(request, 'create-usuario.html', {
            'form': UsuarioForm()
        })
    else:
        try:
            form = UsuarioForm(request.POST)
            new_usuario = form.save(commit=False)
            new_usuario.user=request.user
            new_usuario.save()
            return redirect('usuarios')
        except ValueError:
            return render(request, 'create-usuario.html', {
                'form': UsuarioForm,
                'error': 'Error al crear ussuario'
            })
@login_required
#editar usuario
def usuario_detail(request, usuario_id):
    if request.method=='GET':
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        form=UsuarioForm(instance=usuario)
        return render(request, 'usuario-detail.html',{'usuario':usuario, 'form':form})
    else:
        try:
            usuario=get_object_or_404(Usuario, pk=usuario_id)
            form=UsuarioForm(request.POST, instance=usuario)
            form.save()
            return redirect('usuarios')
        except ValueError:
            return render(request, 'usuario-detail.html', {
                'cliente':usuario,
                'form':form,
                'error': 'Error al editar usuario'
            })

@login_required
#eliminar usuario
def usuario_delete(request, usuario_id):
    usuario=get_object_or_404(Usuario, pk=usuario_id)
    if(request.method=='POST'):
        usuario.delete()
        return redirect('usuarios')