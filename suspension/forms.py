from django import forms
from datetime import datetime

class SuspensionForms(forms.Form):
    reason = forms.CharField(max_length=200, error_messages={'required': 'El campo Razon es requerido', 'max_length': 'El campo Razon debe tener una longitud maxima de 200 caracteres'})
    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'})
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'})

    def clean_finalDate(self):
        data = self.cleaned_data['finalDate']
        if data < datetime.now().date():
            raise forms.ValidationError("La fecha final no puede ser menor a la de hoy")
        return data