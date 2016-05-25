from django import forms

class FineTypeForm(forms.Form):
    reason = forms.CharField(max_length=200, error_messages={'required': 'El campo Razon es requerido', 'max_length': 'El campo Razon debe tener una longitud maxima de 200 caracteres'})
    price = forms.IntegerField(min_value=0, error_messages={'required': 'El campo Precio es requerido', 'min_value':'El campo Precio debe ser mayor o igual a 0'})

class FineForm(forms.Form):
    observations = forms.CharField(max_length=200, error_messages={'required': 'El campo Observaciones es requerido', 'max_length': 'El campo Observaciones debe tener una longitud maxima de 200 caracteres'})
