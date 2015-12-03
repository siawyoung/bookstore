import pdb
from django import forms
from models import *

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = ['login_id', 'password']
        labels = {
            'login_id': 'Username'
        }

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'login_id': 'Username',
            'cc_num': 'Credit Card',
            'phone_num': 'Phone Number'
        }