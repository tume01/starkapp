from django import forms
from .models import Provider

class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = ['ruc','businessName','status','province','distric','registrationDate','address','phone','effectiveTime','email','contactName','contactPhone']

	def __init__(self,*args, **kwargs):
		super(ProviderForm,self).__init__(*args,**kwargs)
		self.fields['ruc'].widget.attrs.update({'class' : 'form-control','id' : 'ruc','name' : 'ruc', 'type' : 'text', 'placeholder' : 'Ingrese el RUC..'})
		self.fields['businessName'].widget.attrs.update({'class' : 'form-control','id' : 'businessName','name' : 'businessName', 'type' : 'text', 'placeholder' : 'Ingrese el nombre de su compañía..'})
		self.fields['status'].widget.attrs.update({'class' : 'form-control','id' : 'status','name' : 'status', 'size' : '1',  'placeholder' : 'Seleccione un estado..'})
		self.fields['province'].widget.attrs.update({'class' : 'form-control','id' : 'province','name' : 'province', 'type' : 'text', 'placeholder' : 'Ingrese la provincia..'})
		self.fields['distric'].widget.attrs.update({'class' : 'form-control','id' : 'distric','name' : 'distric', 'type' : 'text', 'placeholder' : 'Ingrese el distrito..'})
