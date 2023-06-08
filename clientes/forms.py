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
    banco = forms.ChoiceField(choices=bancos, widget=forms.Select(attrs={'class': 'form-select','style': 'width: 300px'}))
    tipoCuenta = forms.ChoiceField(choices=tiposCuenta, widget=forms.Select(attrs={'class': 'form-select','style': 'width: 300px'}))
    regimenTributario = forms.ChoiceField(choices=regimens, widget=forms.Select(attrs={'class': 'form-select','style': 'width: 300px'}))
    
    class Meta:
        model=Cliente
        fields=['rutEmpresa', 'nombreDeFantasia', 'razonSocial','fechaIngresoCliente',
                'claveSII', 'nombreContacto1','telefonoContacto1','emailContacto1',
                'nombreContacto2','telefonoContacto2','emailContacto2',
                'representanteLegal','rutRepresentanteLegal','banco','tipoCuenta',
                'numeroCuenta','claveSIIRepresentante','inicioActividades',
                'regimenTributario','claveCertificadoDigital','vencimientoCertificadoDigital',
                'usuarioPrevired','clavePrevired','otroServicio','estado']
        widgets={
            'rutEmpresa': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'nombreDeFantasia': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'razonSocial': forms.TextInput(attrs={'class':'form-control ', 'style': 'width: 300px'}),
            'fechaIngresoCliente': forms.DateInput(attrs={'class':'form-control','type':'date', 'style': 'width: 300px'}),
            'claveSII': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'nombreContacto1': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'telefonoContacto1': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'emailContacto1': forms.EmailInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'nombreContacto2': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'telefonoContacto2': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'emailContacto2': forms.EmailInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'representanteLegal': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'rutRepresentanteLegal': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            #'banco': forms.TextInput(attrs={'class':'form-control'}),
            #'tipoCuenta': forms.TextInput(attrs={'class':'form-control'}),
            'numeroCuenta': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'claveSIIRepresentante': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'inicioActividades': forms.DateInput(attrs={'class':'form-control','type':'date', 'style': 'width: 300px'}),
            #'regimenTributario': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'claveCertificadoDigital': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'vencimientoCertificadoDigital': forms.DateInput(attrs={'class':'form-control','type':'date', 'style': 'width: 300px'}),
            'usuarioPrevired': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'clavePrevired': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'otroServicio': forms.TextInput(attrs={'class':'form-control', 'style': 'width: 300px'}),
            'estado': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }