from django import forms

class BungalowForm(forms.Form):
    bungalow_type_id = forms.IntegerField(error_messages={'required': 'El tipo de bungalow es requerido'})
    status = forms.IntegerField(error_messages={'required': 'El estado es requerido'})
    number = forms.IntegerField(error_messages={'required': 'El numero de bungalow es requerido'})

# Pending Feature
# class BungalowTypeForm(forms.Form):
#     name = forms.CharField(error_messages={'required': 'El nombre es requerido'})
#     price = forms.FloatField(error_messages={'required': 'El precio es requerido'})
#     capacity = forms.IntegerField(error_messages={'required': 'La capacidad es requerida'})