from django import forms
from django.core.validators import RegexValidator

class MembershipTypeForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

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

    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'})
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'})

