from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator


class MemberForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    name = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 200 caracteres'})
    surname = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Apellidos es requerido', 'max_length': 'El campo Apellidos debe tener una longitud maxima de 200 caracteres'})
    dni = forms.IntegerField(min_value=8, max_value=8, error_messages={'required': 'El campo DNI es requerido', 'min_value':'El campo DNI debe tener 8 digitos minimo', 'max_value':'El campo DNI debe tener 8 digitos como maximo'})
    phone = forms.IntegerField(min_value=8, error_messages={'required': 'El campo Telefono es requerido', 'min_value':'El campo Telefono debe tener minimo 8 digitos'})
    address = forms.CharField(max_length=200, error_messages={'required': 'El campo Direccion es requerido', 'max_length': 'El campo Direccion debe tener una longitud maxima de 200 caracteres'})
    email = forms.CharField(max_length=200,validators=EmailValidator, error_messages={'required': 'El campo Email es requerido', 'max_length': 'El campo Email debe tener una longitud maxima de 200 caracteres'})
