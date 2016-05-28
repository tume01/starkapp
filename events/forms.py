from django import forms

class EventForm(forms.Form):
    name 		= forms.CharField(max_length='20',error_messages={'required': "El nombre del evento es obligatorio.", 'max_length':"El nombre es muy largo"})
    description = forms.CharField(max_length='100',error_messages={'required': "La descripción del evento es obligatorio.",'max_length':"El nombre es muy largo"})
    environment = forms.CharField(error_messages={'required': "El campo ambiente es obligatorio."})
    assistance  = forms.IntegerField(error_messages={'required': "La asistencia es obligatorio."})
    price       = forms.FloatField(error_messages={'required': "El precio es obligatorio."})
    start_date	= forms.DateTimeField(input_formats=["%m/%d/%Y %H:%M %p"], error_messages={'required' : "La fecha de inicio es obligatoria."})
    end_date 	= forms.DateTimeField(input_formats=["%m/%d/%Y %H:%M %p"], error_messages={'required' : "La fecha de inicio es obligatoria."})
    event_type  = forms.CharField(error_messages={'required' : "El tipo de evento es obligatorio."})
    #status      = forms.IntegerField(error_messages={'required': "La estado es obligatorio."})


