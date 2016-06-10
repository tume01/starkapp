from django import forms

class ActivityForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'El campo nombre es requerido'})
    price = forms.CharField(error_messages={'required': 'El campo precio es requerido'})
    end_date = forms.DateTimeField(error_messages={'required': 'El campo fecha fin es requerido'}, input_formats=['%d/%m/%Y %H:%M'])
    attendance = forms.IntegerField(error_messages={'required': 'El campo registrados es requerido'})
    start_date = forms.DateTimeField(error_messages={'required': 'El campo fecha inicio es requerido'}, input_formats=['%d/%m/%Y %H:%M'])
    activity_type = forms.IntegerField()
    environments = forms.IntegerField()