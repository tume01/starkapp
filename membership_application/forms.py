from django import forms
from datetime import datetime
from django.core.validators import RegexValidator
from services.Membership_ApplicationService import Membership_ApplicationService
from services.MemberService import MembersService
from services.AffiliateService import AffiliateService
from django.core.files.images import get_image_dimensions

class MembershipApplicationForm(forms.Form):
    alphabetic = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabetic characters are allowed.')


    firstName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Nombres es requerido', 'max_length': 'El campo Nombres debe tener una longitud maxima de 20 caracteres'})
    paternalLastName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Apellido paterno es requerido', 'max_length': 'El campo Apellido paterno debe tener una longitud maxima de 20 caracteres'})
    maternalLastName = forms.CharField(max_length=20, validators=[alphabetic], error_messages={'required': 'El campo Apellido materno es requerido', 'max_length': 'El campo Apellido materno debe tener una longitud maxima de 20 caracteres'})
    num_doc = forms.IntegerField(error_messages={'required': 'El campo Numero de Documento es requerido'})
    initialDate = forms.DateField(error_messages={'required': 'El campo Fecha inicial es requerido'}, input_formats=['%d/%m/%Y'])
    finalDate = forms.DateField(error_messages={'required': 'El campo Fecha final es requerido'}, input_formats=['%d/%m/%Y'])
    comments = forms.CharField(max_length=200, error_messages={'required': 'El campo Comentarios es requerido', 'max_length': 'El campo Comentarios debe tener una longitud maxima de 200 caracteres'})

    address = forms.CharField(max_length=200, error_messages={'required': 'El campo Direccion es requerido', 'max_length': 'El campo Direccion no debe superar los 200 caracteres'})
    workPlace= forms.CharField(max_length=200, error_messages={'required': 'El campo Centro de trabajo es requerido', 'max_length': 'El campo Centro de trabajo no debe superar los 200 caracteres'})
    workPlaceJob= forms.CharField(max_length=200, error_messages={'required': 'El campo Puesto de trabajo es requerido', 'max_length': 'El campo Puesto de trabajo no debe superar los 200 caracteres'})
    workPlacePhone = forms.IntegerField(error_messages={'required': 'El campo Teléfono de Oficina es requerido'})
    nationality = forms.CharField(max_length=20, error_messages={'required': 'El campo Nacionalidad es requerido', 'max_length': 'El campo Nacionalidad no debe superar los 20 caracteres'})
    maritalStatus = forms.CharField(max_length=20, error_messages={'required': 'El campo Estado civil es requerido', 'max_length': 'El campo Estado civil no debe superar los 20 caracteres'})
    cellphoneNumber = forms.IntegerField(error_messages={'required': 'El campo Teléfono Celular es requerido'})
    specialization = forms.CharField(max_length=200, error_messages={'required': 'El campo Especialización es requerido', 'max_length': 'El campo Especialización no debe superar los 200 caracteres'})

    birthDate = forms.DateField(error_messages={'required': 'El campo Fecha de nacimiento es requerido'}, input_formats=['%d/%m/%Y'])

    birthPlace = forms.CharField(max_length=200, error_messages={'required': 'El campo Lugar de nacimiento es requerido', 'max_length': 'El campo Lugar de nacimiento no debe superar los 200 caracteres'})
    email = forms.CharField(max_length=200, error_messages={'required': 'El campo Correo es requerido', 'max_length': 'El campo Correo no debe superar los 200 caracteres'})
    phone = forms.IntegerField(error_messages={'required': 'El campo Numero de telefono es requerido'})
    photo = forms.ImageField(required=False)

    snum_doc = forms.IntegerField( required=False)
    sbirthDate = forms.DateField( required=False, input_formats=['%d/%m/%Y'])
    sfirstName = forms.CharField(max_length=20, required=False, validators=[alphabetic], error_messages={'max_length': 'El campo Nombres debe tener una longitud maxima de 20 caracteres'})
    spaternalLastName = forms.CharField(max_length=20,required=False, validators=[alphabetic], error_messages={'max_length': 'El campo Apellido paterno debe tener una longitud maxima de 20 caracteres'})
    smaternalLastName = forms.CharField(max_length=20, required=False, validators=[alphabetic], error_messages={'max_length': 'El campo Apellido materno debe tener una longitud maxima de 20 caracteres'})
    sspecialization = forms.CharField(max_length=200, required=False, error_messages={'max_length': 'El campo Especialización no debe superar los 200 caracteres'})
    snationality = forms.CharField(max_length=20,required=False, error_messages={'max_length': 'El campo Nacionalidad no debe superar los 20 caracteres'})
    sbirthPlace = forms.CharField(max_length=200,required=False, error_messages={'max_length': 'El campo Lugar de nacimiento no debe superar los 200 caracteres'})
    sworkPlace = forms.CharField(max_length=200,required=False, error_messages={'max_length': 'El campo Centro de trabajo no debe superar los 200 caracteres'})
    sworkPlaceJob = forms.CharField(max_length=200,required=False, error_messages={'max_length': 'El campo Puesto de trabajo no debe superar los 200 caracteres'})
    semail = forms.CharField(max_length=200, required=False,error_messages={'max_length': 'El campo Correo no debe superar los 200 caracteres'})
    scellPhoneNumber = forms.IntegerField(required=False)
    sphoto = forms.ImageField(required=False)
    sdocument_number = forms.IntegerField(required=False)

    def clean_photo(self):
        data = self.cleaned_data["photo"]
        if data == None:
            return data
        w, h = get_image_dimensions(data)
        if w > 301:
            raise forms.ValidationError("Error en el ancho de la imagen")
        if h > 301:
            raise forms.ValidationError("Error en la alutra de la imgen")
        return data

    def clean_sphoto(self):
        data = self.cleaned_data["sphoto"]
        if data == None:
            return data
        w, h = get_image_dimensions(data)
        if w > 301:
            raise forms.ValidationError("Error en el ancho de la imagen del conyuge")
        if h > 301:
            raise forms.ValidationError("Error en la alutra de la imgen del conyuge")
        return data

    def clean_birthDate(self):
        data = self.cleaned_data['birthDate']
        if (data > datetime.now().date()):
            raise forms.ValidationError("La fecha de nacimiento no puede ser mayor a la de hoy")
        return data

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

    def clean_workPlacePhone(self):
        data = self.cleaned_data['workPlacePhone']

        if data is None:
            return None
        
        if (data <= 999999):
            raise forms.ValidationError("El numero de telefono de oficina tiene que tener como mínimo 7 digitos")
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']

        if data is None:
            return None
        
        if (data <= 999999):
            raise forms.ValidationError("El numero de telefono de casa tiene que tener como minimo 7 digitos")
        return data

    def clean_cellphoneNumber(self):
        data = self.cleaned_data['cellphoneNumber']

        if data is None:
            return None
        
        if (data <= 99999999):
            raise forms.ValidationError("El numero de celular tiene que tener como mínimo 9 digitos")
        return data

    def clean_finalDate(self):
        data = self.cleaned_data['finalDate']
        if data < datetime.now().date():
            raise forms.ValidationError("La fecha final no puede ser menor a la de hoy")
        return data

