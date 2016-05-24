from django import forms

class ActivityForm(forms.Form):
    price = forms.CharField(error_messages={'required': 'El campo precio es requerido'})
    end_date = forms.DateTimeField(error_messages={'required': 'El campo fecha fin es requerido'})
    attendance = forms.IntegerField(error_messages={'required': 'El campo registrados es requerido'})
    start_date = forms.DateTimeField(error_messages={'required': 'El campo fecha inicio es requerido'})