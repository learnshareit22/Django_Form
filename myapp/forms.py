from django import forms

class UserForm(forms.Form):
    full_name = forms.CharField(label='Full Name')
    email = forms.CharField(label='Email') # <-- Remove request here
