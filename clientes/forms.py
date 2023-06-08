from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    bancos=(
        ('', 'Seleccione un banco'),
        ('estado', 'Banco Estado'),
        ('santander', 'Banco Santander'),
        ('chile', 'Banco de Chile'),
        ('bci', 'Banca BCI'),
    )
    regimens=(
        ('', 'Seleccione un tipo de regimen'),
        ('proPymeGenereal', 'Pro Pyme General 14A'),
        ('semiIntegrado', 'Semi integrado 14A'),
        ('otro', 'Otro tipo de regimen')
    )
    tiposCuenta=(
        ('', 'Seleccione un tipo de cuenta'),
        ('vista', 'Cuenta Vista'),
        ('otro', 'Otro tipo de cuenta'),
    )
    banco = forms.ChoiceField(choices=bancos, widget=forms.Select(attrs={'class': 'form-select'}))
    tipoCuenta = forms.ChoiceField(choices=tiposCuenta, widget=forms.Select(attrs={'class': 'form-select'}))
    regimenTributario = forms.ChoiceField(choices=regimens, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model=Cliente
        fields=['rutEmpresa', 'nombreDeFantasia', 'razonSocial','fechaIngresoCliente',
                'claveSII', 'nombreContacto1','telefonoContacto1','emailContacto1',
                'nombreContacto2','telefonoContacto2','emailContacto2',
                'representanteLegal','rutRepresentanteLegal','banco','tipoCuenta',
                'numeroCuenta','claveSIIRepresentante','inicioActividades',
                'regimenTributario','claveCertificadoDigital','vencimientoCertificadoDigital',
                'usuarioPrevired','clavePrevired','servicioContable','servicioRemuneraciones',
                'ServicioPortalRRHH','otroServicio','estado']
        widgets={
            'rutEmpresa': forms.TextInput(attrs={'class':'form-control'}),
            'nombreDeFantasia': forms.TextInput(attrs={'class':'form-control'}),
            'razonSocial': forms.TextInput(attrs={'class':'form-control'}),
            'fechaIngresoCliente': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'claveSII': forms.TextInput(attrs={'class':'form-control'}),
            'nombreContacto1': forms.TextInput(attrs={'class':'form-control'}),
            'telefonoContacto1': forms.TextInput(attrs={'class':'form-control'}),
            'emailContacto1': forms.EmailInput(attrs={'class':'form-control'}),
            'nombreContacto2': forms.TextInput(attrs={'class':'form-control'}),
            'telefonoContacto2': forms.TextInput(attrs={'class':'form-control'}),
            'emailContacto2': forms.EmailInput(attrs={'class':'form-control'}),
            'representanteLegal': forms.TextInput(attrs={'class':'form-control'}),
            'rutRepresentanteLegal': forms.TextInput(attrs={'class':'form-control'}),
            #'banco': forms.TextInput(attrs={'class':'form-control'}),
            #'tipoCuenta': forms.TextInput(attrs={'class':'form-control'}),
            'numeroCuenta': forms.TextInput(attrs={'class':'form-control'}),
            'claveSIIRepresentante': forms.TextInput(attrs={'class':'form-control'}),
            'inicioActividades': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            #'regimenTributario': forms.TextInput(attrs={'class':'form-control'}),
            'claveCertificadoDigital': forms.TextInput(attrs={'class':'form-control'}),
            'vencimientoCertificadoDigital': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'usuarioPrevired': forms.TextInput(attrs={'class':'form-control'}),
            'clavePrevired': forms.TextInput(attrs={'class':'form-control'}),
            'servicioContable': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'servicioRemuneraciones': forms.NumberInput(attrs={'class':'form-control'}),
            'ServicioPortalRRHH': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'otroServicio': forms.TextInput(attrs={'class':'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }