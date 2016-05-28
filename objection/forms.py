from django import forms
from datetime import datetime
from services.Membership_ApplicationService import Membership_ApplicationService

class ObjectionForm(forms.Form):
    comments = forms.CharField(max_length=200, error_messages={'required': 'El campo Comentarios es requerido', 'max_length': 'El campo Comentarios debe tener una longitud maxima de 200 caracteres'})

    def clean(self):
        idMembership = self.data['id_membership']

        member_application_service = Membership_ApplicationService()

        membership_application = member_application_service.getMembership_Application(idMembership)

        finalDate = membership_application.finalDate

        if (finalDate < datetime.now().date()):
            raise forms.ValidationError("La fecha limite ya se cumplio. No se pueden ingresar mas comentarios")
        return finalDate

