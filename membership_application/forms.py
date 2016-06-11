from django import forms
from datetime import datetime
from django.core.validators import RegexValidator
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MemberService import MembersService
from services.AffiliateService import AffiliateService

class MembershipApplicationForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')


    firstName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 20 caracteres'})
    paternalLastName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Apellido paterno es requerido', 'max_length': 'El campo Apellido paterno debe tener una longitud maxima de 20 caracteres'})
    maternalLastName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Apellido materno es requerido', 'max_length': 'El campo Apellido materno debe tener una longitud maxima de 20 caracteres'})
    num_doc = forms.IntegerField(error_messages={'required': 'El campo Numero de Documento es requerido'})
    comments = forms.CharField(max_length=200, error_messages={'required': 'El campo Comentarios es requerido', 'max_length': 'El campo Comentarios debe tener una longitud maxima de 200 caracteres'})
    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'})
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'})

    def clean_dni(self):
        data = self.cleaned_data['num_doc']
        if (data < 9999999):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")
        if (data > 100000000):
            raise forms.ValidationError("El dni tiene que tener 8 digitos")

        membership_applicationService = Membership_ApplicationService()

        existingMembershipApplication = membership_applicationService.find(num_doc=data)

        members_service = MembersService()

        existingMember = members_service.find(num_doc=data)

        affiliate_service = AffiliateService()

        existingAffiliate = affiliate_service.find(num_doc=data)

        if(existingMembershipApplication != None):
            raise forms.ValidationError("El numero de documento ingresado ya existe y ha"+
                                        "solicitado una membresia")
        if(existingMember != None):
            raise forms.ValidationError("El numero de documento ingresado ya existe y"+
                                        "es un miembro")
        if(existingAffiliate != None):
            raise forms.ValidationError("El numero de documento ingresado ya existe y esta"+
                                        "afiliado al miembro "+existingAffiliate.member.name + " "+
                                        existingAffiliate.member.paternalLastName + " "+
                                        existingAffiliate.member.maternalLastName)
        
        return data

    def clean_finalDate(self):
        data = self.cleaned_data['finalDate']
        if data < datetime.now().date():
            raise forms.ValidationError("La fecha final no puede ser menor a la de hoy")
        return data

