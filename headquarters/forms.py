from django import forms

class HeadquarterForm(forms.Form):
	name = forms.CharField(error_messages={'required': 'El campo nombre es requerido'})
	description = forms.CharField(error_messages={'required': 'El campo descripcion es requerido'})
	location = forms.CharField(error_messages={'required': 'El campo lugar es requerido'})