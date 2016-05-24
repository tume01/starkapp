from django import forms

class MembershipTypeForm(forms.Form):
    name = forms.CharField(max_length=200, error_messages={'required': 'El campo tipo de membresia es requerido', 'max_length': 'El campo tipo de membresia debe tener una longitud maxima de 200 caracteres'})
    guests = forms.IntegerField(min_value=0, error_messages={'required': 'El campo invitados es requerido', 'min_value':'El campo invitados debe ser mayor o igual a 0'})
    price = forms.FloatField(min_value=0, error_messages={'required': 'El campo precio es requerido', 'min_value': 'El campo precio debe ser mayor o igual a 0'})
    billing = forms.CharField(max_length=200, error_messages={'required': 'El campo tipo de cobro es requerido', 'max_length': 'El campo tipo de combro debe tener una longitud maxima de 200 caracteres'})
