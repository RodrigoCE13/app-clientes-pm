from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm
from .models import Cliente
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q

# Create your views here.



@login_required
#listar clientes
def clientes(request):
    queryset = request.GET.get("buscar")
    print(queryset)
    clientes = Cliente.objects.filter(estado=True) 
    if queryset:
        clientes=Cliente.objects.filter(
            Q(nombreDeFantasia__icontains= queryset)
        ).distinct()   
    clientes=Cliente.objects.all()#en caso de quere mostrar solo los datos del usuario logeado ""Cliente.objects.filter(user=request.user)""
    return render(request, 'clientes.html',{'clientes':clientes})
@login_required
#crear clientes
@csrf_protect
def create_clientes(request):
    if request.method == 'GET':
        return render(request, 'create-cliente.html', {
            'form': ClienteForm()
        })
    else:
        try:
            form = ClienteForm(request.POST)
            new_cliente = form.save(commit=False)
            new_cliente.user = request.user
            new_cliente.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'create-cliente.html', {
                'form': ClienteForm(),
                'error': 'Error al crear cliente'
            })

@login_required
#editar clientes
def cliente_detail(request, cliente_id):
    if request.method=='GET':
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        form=ClienteForm(instance=cliente)
        return render(request, 'cliente-detail.html',{'cliente':cliente, 'form':form})
    else:
        try:
            cliente=get_object_or_404(Cliente, pk=cliente_id)
            form=ClienteForm(request.POST, instance=cliente)
            form.save()
            return redirect('clientes')
        except ValueError:
            return render(request, 'cliente-detail.html', {
                'cliente':cliente,
                'form':form,
                'error': 'Error al editar cliente'
            })

@login_required
#eliminar clientes
def cliente_delete(request, cliente_id):
    cliente=get_object_or_404(Cliente, pk=cliente_id)
    if(request.method=='POST'):
        cliente.delete()
        return redirect('clientes')
    

def verCliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'vercliente.html', {'cliente': cliente})


