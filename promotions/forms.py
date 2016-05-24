from django import forms

class PromotionForm(forms.Form):
    description = forms.CharField(max_length=200, error_messages={'required': 'El campo promocion es requerido', 'max_length': 'El campo promocion debe tener una longitud maxima de 200 caracteres'})
    percentage = forms.FloatField(min_value=0, max_value=100, error_messages={'required': 'El campo descuento es requerido', 'min_value': 'El campo descuento debe ser mayor o igual a 0%', 'max_value': 'El campo descuento debe ser menor o igual a 100%'})
