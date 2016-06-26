from django import forms
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator


class AffiliateForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Solo caracteres alfabeticos estan perimitidos para los campos Nombre y Apellidos.')

    name = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 200 caracteres'})
    paternalLastName = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Apellido paterno es requerido', 'max_length': 'El campo Apellido paterno debe tener una longitud maxima de 200 caracteres'})
    maternalLastName = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Apellido materno es requerido', 'max_length': 'El campo Apellido materno debe tener una longitud maxima de 200 caracteres'})
    num_doc = forms.IntegerField( error_messages={'required': 'El campo Numero de Documento es requerido'})
    phone = forms.IntegerField(error_messages={'required': 'El campo Telefono es requerido'})
    address = forms.CharField(max_length=200, error_messages={'required': 'El campo Direccion es requerido', 'max_length': 'El campo Direccion debe tener una longitud maxima de 200 caracteres'})
    email = forms.CharField(max_length=200, error_messages={'required': 'El campo Email es requerido', 'max_length': 'El campo Email debe tener una longitud maxima de 200 caracteres'})

    workPlace = forms.CharField(required=False, max_length=200, error_messages={'max_length': 'El campo Centro de trabajo no debe superar los 200 caracteres'})
    workPlaceJob = forms.CharField(required=False, max_length=200, error_messages={'max_length': 'El campo Puesto de trabajo no debe superar los 200 caracteres'})
    workPlacePhone = forms.IntegerField(required=False)
    nationality = forms.CharField(max_length=20, error_messages={'required': 'El campo Nacionalidad es requerido', 'max_length': 'El campo Nacionalidad no debe superar los 20 caracteres'})
    maritalStatus = forms.CharField(required=False, max_length=20, error_messages={'max_length': 'El campo Estado civil no debe superar los 20 caracteres'})
    cellphoneNumber = forms.IntegerField(required=False)
    specialization = forms.CharField(max_length=200, error_messages={'max_length': 'El campo Especialización no debe superar los 200 caracteres'})
    birthDate = forms.DateField(error_messages={'required': 'El campo Fecha de nacimiento es requerido'})
    birthPlace = forms.CharField(max_length=200, error_messages={'required': 'El campo Lugar de nacimiento es requerido', 'max_length': 'El campo Lugar de nacimiento no debe superar los 200 caracteres'})

    def clean_dni(self):
        data = self.cleaned_data['num_doc']
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
