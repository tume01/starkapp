from django import forms

class PoliticForm(forms.Form):
    name  = forms.CharField(error_messages  = {'required': 'El nombre es requerido'})
    value = forms.FloatField(error_messages = {'required': 'El valor es requerido'})
