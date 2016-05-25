from django import forms

class MembershipTypeForm(forms.Form):
    name = forms.CharField(max_length=200, error_messages={'required': 'El campo Tipo de Membresia es requerido', 'max_length': 'El campo Tipo de Membresia debe tener una longitud maxima de 200 caracteres'})
    guests = forms.IntegerField(min_value=0, error_messages={'required': 'El campo Invitados es requerido', 'min_value':'El campo Invitados debe ser mayor o igual a 0'})
    price = forms.FloatField(min_value=0, error_messages={'required': 'El campo Precio es requerido', 'min_value': 'El campo precio debe ser mayor o igual a 0'})
    billing = forms.CharField(max_length=200, error_messages={'required': 'El campo Tipo de cobro es requerido', 'max_length': 'El campo Tipo de combro debe tener una longitud maxima de 200 caracteres'})

class MembershipForm(forms.Form):

    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'})
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'})

    def clean(self):
        initialDate = self.cleaned_data['initialDate']
        finalDate = self.cleaned_data['finalDate']
        if initialDate > finalDate:
            raise forms.ValidationError("Fecha inicial mayor que fecha final!")
