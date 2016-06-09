from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group, User

class UserForm(forms.Form):
    #alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')
    # validators=[alphabetic],

    name = forms.CharField(max_length=200,
                           error_messages={'required': 'El campo usuario es requerido',
                                           'max_length': 'El campo usuario debe tener una longitud maxima de 200 caracteres'})
    password = forms.CharField(max_length=200,
                               error_messages={'required': 'El campo contraseña es requerido',
                                               'max_length': 'El campo contraseña debe tener una longitud maxima de 200 caracteres'})

    user_type = forms.IntegerField(error_messages={'required': 'El campo tipo de usuario es requerido'})
        

class UserTypeForm(forms.Form):
    name = forms.CharField(max_length=200,
                           error_messages={'required': 'El campo nombre es requerido',
                                           'max_length': 'El campo nombre debe tener una longitud maxima de 200 caracteres'})
