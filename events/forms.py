from django import forms

class EventForm(forms.Form):
    name 		= forms.CharField(max_length='20',error_messages={'required': "El nombre del evento es obligatorio.", 'max_length':"El nombre es muy largo"})
    description = forms.CharField(max_length='100',error_messages={'required': "La descripción del evento es obligatorio.",'max_length':"El nombre es muy largo"})
    environment = forms.CharField(error_messages={'required': "La descripción del evento es obligatorio."})
    assistance  = forms.IntegerField(error_messages={'required': "La descripción del evento es obligatorio."})
    price       = forms.FloatField(error_messages={'required': "La descripción del evento es obligatorio."})
    status      = forms.IntegerField(error_messages={'required': "La descripción del evento es obligatorio."})


