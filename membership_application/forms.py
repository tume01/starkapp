from django import forms
from django.core.validators import RegexValidator

class MembershipApplication(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    firstName = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 200 caracteres'})
    lastName = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo Apellidos es requerido', 'max_length': 'El campo Apellidos debe tener una longitud maxima de 200 caracteres'})
    dni = forms.IntegerField(min_value=8, max_value=8, error_messages={'required': 'El campo DNI es requerido', 'min_value':'El campo DNI debe tener 8 digitos minimo', 'max_value':'El campo DNI debe tener 8 digitos como maximo'})
    comments = forms.CharField(max_length=200, error_messages={'required': 'El campo Comentarios es requerido', 'max_length': 'El campo Comentarios debe tener una longitud maxima de 200 caracteres'})
    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'})
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'})

    def clean(self):
        initialDate = self.cleaned_data['initialDate']
        finalDate = self.cleaned_data['finalDate']
        if initialDate > finalDate:
            raise forms.ValidationError("Fecha inicial mayor que fecha final!")


