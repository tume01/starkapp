from django import forms

class ObjectionForm(forms.Form):
    comments = forms.CharField(max_length=200, error_messages={'required': 'El campo Comentarios es requerido', 'max_length': 'El campo Comentarios debe tener una longitud maxima de 200 caracteres'})