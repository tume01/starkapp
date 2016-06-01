from django import forms

class FineTypeForm(forms.Form):
    reason = forms.CharField(max_length=200, error_messages={'required': 'El campo Razon es requerido', 'max_length': 'El campo Razon debe tener una longitud maxima de 200 caracteres'})
    price = forms.FloatField(error_messages={'required': 'El campo Precio es requerido'})

    def clean_price(self):
        data = self.cleaned_data['price']
        if (data < 0):
            raise forms.ValidationError("El precio tiene que ser mayor que 0")
        return data

class FineForm(forms.Form):
    observations = forms.CharField(max_length=200, error_messages={'required': 'El campo Observaciones es requerido', 'max_length': 'El campo Observaciones debe tener una longitud maxima de 200 caracteres'})
