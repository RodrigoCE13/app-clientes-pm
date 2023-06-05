from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    roles=(
        ('', 'Seleccione un tipo de usuario'),
        ('UserPm', 'Usuario Pyme manager'),
        ('UserClient', 'Usuario Cliente'),
        ('UserAdmin', 'Usuario Administrador')
    )
    rol_usuario = forms.ChoiceField(choices=roles, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model=Usuario
        fields=['nombre', 'apellido','password','email', 'rol_usuario', 'estado']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }