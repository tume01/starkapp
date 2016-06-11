from django import forms

class ServicioForm(forms.Form):
    id_servicio = forms.IntegerField(error_messages={'required': 'El tipo de servicios es requerido'})
    name = forms.CharField(error_messages={'required': 'El nombre es requerido'})
    price = forms.FloatField(error_messages={'required': 'El precio es requerido'})

class UpdateServicioForm(forms.Form):
    price = forms.FloatField(error_messages={'required': 'El precio es requerido'})
    name = forms.CharField(error_messages={'required': 'El nombre es requerido'})

# Pending Features
# class BungalowTypeForm(forms.Form):
#     name = forms.CharField(error_messages={'required': 'El nombre es requerido'})
#     price = forms.FloatField(error_messages={'required': 'El precio es requerido'})
#     capacity = forms.IntegerField(error_messages={'required': 'La capacidad es requerida'})