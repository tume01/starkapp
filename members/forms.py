from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator


class MemberForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Solo caracteres alfabeticos estan perimitidos para los campos Nombre y Apellidos.')

    name = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 200 caracteres'})
    surname = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Apellidos es requerido', 'max_length': 'El campo Apellidos debe tener una longitud maxima de 200 caracteres'})
    dni = forms.IntegerField( error_messages={'required': 'El campo DNI es requerido'})
    phone = forms.IntegerField(error_messages={'required': 'El campo Telefono es requerido'})
    address = forms.CharField(error_messages={'required': 'El campo Direccion es requerido'})
    email = forms.CharField(max_length=200, error_messages={'required': 'El campo Email es requerido', 'max_length': 'El campo Email debe tener una longitud maxima de 200 caracteres'})

    def clean_dni(self):
        data = self.cleaned_data['dni']
        if (data < 9999999):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")
        if (data > 100000000):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if (data < 0):
            raise forms.ValidationError("El Telefono no puede ser negativo")
        if (data < 999999):
            raise forms.ValidationError("El Telefono tiene que ser como minimo 7 digitos")
        return data