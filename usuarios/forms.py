from django import forms
from .models import Usuario
from clientes.models import Cliente

class UsuarioForm(forms.ModelForm):
    roles=(
        ('', 'Seleccione un tipo de usuario'),
        ('UserPm', 'Usuario Pyme manager'),
        ('UserClient', 'Usuario Cliente'),
        ('UserAdmin', 'Usuario Administrador')
    )
    rol_usuario = forms.ChoiceField(choices=roles, widget=forms.Select(attrs={'class': 'form-select shadow-sm','onchange':'selectCliente()'}))
    cliente= forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True), empty_label="Seleccione un cliente", widget=forms.Select(attrs={'class': 'form-select shadow-sm'}),required=False)
    class Meta:
        model=Usuario
        fields=['nombre', 'apellido','email','rol_usuario', 'nombreDeUsuario','password','cliente', 'estado']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'apellido': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'email': forms.EmailInput(attrs={'class':'form-control shadow-sm'}),
            'nombreDeUsuario': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'password': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input shadow-sm'}),
        }