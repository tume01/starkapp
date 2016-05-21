from django import forms

class ActivityForm(forms.Form):
    description = forms.CharField()
    price = forms.CharField()