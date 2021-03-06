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

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn',
            'title',
            'authors',
            'publisher',
            'year_op',
            'copies',
            'price',
            'b_format',
            'keywords',
            'subject']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date_time','customer']

class OrderBookForm(forms.ModelForm):
    class Meta:
        model = Order_book
        fields = ['order', 'book', 'copies']