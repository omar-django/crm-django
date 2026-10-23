from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput , TextInput 
from.models import Record

# Register User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


# Login User
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password =forms.CharField(widget=PasswordInput())


class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name' , 'last_name' , 'phone', 'email', 'address', 'category' , 'status' , 'notes']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter first name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter last name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '01012345678',
                'inputmode': 'tel',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'status': forms.Select(attrs={
                'class': 'form-select',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter notes',
                'rows': 3
            }),    
        }




class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name' , 'last_name' , 'phone', 'email', 'address', 'category' , 'status' , 'notes']

        widgets = {
            'phone': forms.TextInput(attrs={'inputmode': 'numeric'}),
        }
