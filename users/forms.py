from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=200, error_messages={'required': 'El campo usuario es requerido', 'max_length': 'El campo usuario debe tener una longitud maxima de 200 caracteres'})
    password = forms.CharField(max_length=200, error_messages={'required': 'El campo contraseña es requerido', 'max_length': 'El campo contraseña debe tener una longitud maxima de 200 caracteres'})
