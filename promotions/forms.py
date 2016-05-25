from django import forms
from django.core.validators import MaxValueValidator

class PromotionForm(forms.Form):
    description = forms.CharField(max_length=200, error_messages={'required': 'El campo promocion es requerido',
                                                                  'max_length': 'El campo promocion debe tener una longitud maxima de 200 caracteres'})
    percentage = forms.FloatField(error_messages={'required': 'El campo descuento es requerido'})

    def clean_percentage(self):
        data = self.cleaned_data['percentage']
        if (data < 0):
            raise forms.ValidationError("El porcentaje tiene que ser mayor que 0")
        if (data > 100):
            raise forms.ValidationError("El porcentaje tiene que ser menor que 100")
        return data