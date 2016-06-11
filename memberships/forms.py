from django import forms
from datetime import datetime
from django.core.validators import RegexValidator

class MembershipTypeForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Solo caracteres alfabeticos estan perimitidos para los campos Nombre y Apellidos.')

    name = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Tipo de Membresia es requerido', 'max_length': 'El campo Tipo de Membresia debe tener una longitud maxima de 200 caracteres'})
    guests = forms.IntegerField(error_messages={'required': 'El campo Invitados es requerido'})
    price = forms.FloatField(error_messages={'required': 'El campo Precio es requerido'})
    billing = forms.CharField(max_length=200,  error_messages={'required': 'El campo Tipo de cobro es requerido', 'max_length': 'El campo Tipo de combro debe tener una longitud maxima de 200 caracteres'})

    def clean_guests(self):
        data = self.cleaned_data['guests']
        if (data < 0):
            raise forms.ValidationError("El campo de Invitados tiene que ser mayor que 0")
        return data

    def clean_price(self):
        data = self.cleaned_data['price']
        if (data < 0):
            raise forms.ValidationError("El campo Precio tiene que ser mayor que 0")
        return data

class MembershipForm(forms.Form):

    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'}, input_formats=['%m/%d/%Y'])
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'}, input_formats=['%m/%d/%Y'])

    def clean_finalDate(self):
        data = self.cleaned_data['finalDate']
        if data < datetime.now().date():
            raise forms.ValidationError("La fecha final no puede ser menor a la de hoy")
        return data
