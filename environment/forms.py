from django import forms
from django.forms import ModelChoiceField
from .models import Environment

class EnvironmentForm(forms.ModelForm):

	#region = ModelChoiceField(queryset = Region.objects.all())

	class Meta:
		model = Environment
		fields = ['name','capacity','status','description'] #'headquarter'
		


	def __init__(self,*args, **kwargs):
		super(EnvironmentForm,self).__init__(*args,**kwargs)

		self.fields['name'].widget.attrs.update({'class' : 'form-control','id' : 'name','name' : 'name', 'type' : 'text', 'placeholder' : 'Ingrese el nombre..'})
		self.fields['capacity'].widget.attrs.update({'class' : 'form-control','id' : 'capacity','name' : 'capacity', 'type' : 'number','min' : '0', 'placeholder' : 'Ingrese el aforo..'})
		self.fields['status'].widget.attrs.update({'class' : 'form-control','id' : 'status','name' : 'status', 'size' : '1',  'placeholder' : 'Seleccione un estado..'})
		#self.fields['headquarter'].widget.attrs.update({'class' : 'form-control','id' : 'headquarter','name' : 'headquarter', 'size' : '1', 'placeholder' : 'Seleccione la sede..'})
		self.fields['description'].widget.attrs.update({'class' : 'form-control','id' : 'description','name' : 'description', 'type' : 'text', 'placeholder' : 'Ingrese una descripción..'})
		#'style':'text-align:right;'
