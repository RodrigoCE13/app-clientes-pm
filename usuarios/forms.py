from django.contrib.auth.forms import UserCreationForm
from django import forms

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')