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
    birthDate = forms.DateField(error_messages={'required': 'El campo Fecha de nacimiento es requerido'}, input_formats=['%d/%m/%Y'])
    birthPlace = forms.CharField(max_length=200, error_messages={'required': 'El campo Lugar de nacimiento es requerido', 'max_length': 'El campo Lugar de nacimiento no debe superar los 200 caracteres'})

    def clean_dni(self):
        data = self.cleaned_data['num_doc']
        if (data < 9999999):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")
        if (data > 100000000):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")
        return data

    def clean_workPlacePhone(self):
        data = self.cleaned_data['workPlacePhone']
        if (data < 999999):
            raise forms.ValidationError("El numero de telefono de oficina tiene que tener 7 digitos")
        if (data > 10000000):
            raise forms.ValidationError("El numero de telefono de oficina tiene que tener 7 digitos")
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if (data < 999999):
            raise forms.ValidationError("El numero de telefono de casa tiene que tener 7 digitos")
        if (data > 10000000):
            raise forms.ValidationError("El numero de telefono de casa tiene que tener 7 digitos")
        return data

    def clean_cellphoneNumber(self):
        data = self.cleaned_data['cellphoneNumber']
        if (data < 99999999):
            raise forms.ValidationError("El numero de celular tiene que tener 9 digitos")
        if (data > 1000000000):
            raise forms.ValidationError("El numero de celular tiene que tener 9 digitos")
        return data
