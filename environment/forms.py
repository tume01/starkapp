from django import forms
from django.core.validators import RegexValidator

class EnvironmentForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')

    name = forms.CharField(max_length=200, validators=[alphabetic], error_messages={'required': 'El campo nombre es requerido', 'max_length': 'El campo Tipo de Membresia debe tener una longitud maxima de 200 caracteres'})
    capacity = forms.IntegerField(error_messages={'required': 'El campo aforo es requerido'})
    description = forms.CharField(max_length=200,  error_messages={'required': 'El campo descripcion es requerido', 'max_length': 'El campo Tipo de combro debe tener una longitud maxima de 200 caracteres'})

    def clean_capacity(self):
        data = self.cleaned_data['capacity']
        if (data < 0):
            raise forms.ValidationError("El campo de Aforo tiene que ser mayor que 0")
        return data

class EnvReservationForm(forms.Form):
    price = forms.CharField(error_messages={'required': 'El campo precio es requerido'})
    end_date = forms.DateTimeField(error_messages={'required': 'El campo fecha fin es requerido'}, input_formats=['%m/%d/%Y'])
    start_date = forms.DateTimeField(error_messages={'required': 'El campo fecha inicio es requerido'}, input_formats=['%m/%d/%Y'])
    environment_id = forms.IntegerField()