from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    bancos=(
        ('', 'Seleccione un banco'),
        ('estado', 'Banco Estado'),
        ('santander', 'Banco Santander'),
        ('chile', 'Banco de Chile'),
        ('bci', 'Banca BCI'),
        ('otro', 'Otro banco')
    )
    regimens=(
        ('', 'Seleccione un tipo de regimen'),
        ('Atribuida 14A', 'Atribuida 14A'),
        ('Pro Pyme General 14D', 'Pro Pyme General 14D'),
        ('Semi integrado 14A', 'Semi integrado 14A'),
        ('Renta presunta', 'Renta presunta'),
        ('otro', 'Otro tipo de regimen')
    )
    tiposCuenta=(
        ('', 'Seleccione un tipo de cuenta'),
        ('vista', 'Cuenta Vista'),
        ('Rut', 'Cuenta Rut'),
        ('Corriente', 'Cuenta Corriente'),
        ('otro', 'Otro tipo de cuenta'),
    )
    banco = forms.ChoiceField(choices=bancos, widget=forms.Select(attrs={'class': 'form-select shadow-sm'}), required=False)
    tipoCuenta = forms.ChoiceField(choices=tiposCuenta, widget=forms.Select(attrs={'class': 'form-select shadow-sm'}), required=False)
    regimenTributario = forms.ChoiceField(choices=regimens, widget=forms.Select(attrs={'class': 'form-select shadow-sm border border-primary'}))
    
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
            'rutEmpresa': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'nombreDeFantasia': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'razonSocial': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'fechaIngresoCliente': forms.DateInput(attrs={'class':'form-control shadow-sm border border-primary','type':'date'}),
            'claveSII': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'nombreContacto1': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'telefonoContacto1': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'emailContacto1': forms.EmailInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'nombreContacto2': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'telefonoContacto2': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'emailContacto2': forms.EmailInput(attrs={'class':'form-control shadow-sm'}),
            'representanteLegal': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            'rutRepresentanteLegal': forms.TextInput(attrs={'class':'form-control shadow-sm border border-primary'}),
            #'banco': forms.TextInput(attrs={'class':'form-control'}),
            #'tipoCuenta': forms.TextInput(attrs={'class':'form-control'}),
            'numeroCuenta': forms.TextInput(attrs={'class':'form-control'}),
            'claveSIIRepresentante': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'inicioActividades': forms.DateInput(attrs={'class':'form-control shadow-sm border border-primary','type':'date'}),
            #'regimenTributario': forms.TextInput(attrs={'class':'form-control'}),
            'claveCertificadoDigital': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'vencimientoCertificadoDigital': forms.DateInput(attrs={'class':'form-control shadow-sm','type':'date'}),
            'usuarioPrevired': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'clavePrevired': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'servicioContable': forms.CheckboxInput(attrs={'class':'form-check-input shadow-sm'}),
            'servicioRemuneraciones': forms.NumberInput(attrs={'class':'form-control shadow-sm'}),
            'ServicioPortalRRHH': forms.CheckboxInput(attrs={'class':'form-check-input shadow-sm'}),
            'otroServicio': forms.TextInput(attrs={'class':'form-control shadow-sm'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input shadow-sm'}),
        }