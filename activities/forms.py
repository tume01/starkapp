from django import forms

class ActivityForm(forms.Form):
    description = forms.CharField(error_messages={'required': 'El campo descripcion es requerido'})
    price = forms.CharField(error_messages={'required': 'El campo precio es requerido'})