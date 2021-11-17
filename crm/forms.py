from django import forms

class OrderForms(forms.Form):
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs= {'class': 'form-control'}))
    phone = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs= {'class': 'form-control'}))
