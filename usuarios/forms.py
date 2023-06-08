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
    rol_usuario = forms.ChoiceField(choices=roles, widget=forms.Select(attrs={'class': 'form-select'}))
    cliente= forms.ModelChoiceField(queryset=Cliente.objects.filter(estado=True), empty_label="Seleccione un cliente", widget=forms.Select(attrs={'class': 'form-select'}),required=False)
    class Meta:
        model=Usuario
        fields=['nombre', 'apellido','email','rol_usuario', 'nombreDeUsuario','password','cliente', 'estado']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'nombreDeUsuario': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }