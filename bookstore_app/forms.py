from django import forms
from models import *

class LoginForm(forms.ModelForm):
    # username = forms.CharField(label='Username', max_length=20)
    # password = forms.PasswordInput()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ['login_id', 'password']
        labels = {
            'login_id': 'Username'
        }