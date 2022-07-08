from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateAccountForm(UserCreationForm):

    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': "form-control form-control-lg form-control-solid",
            'placeholder': "analytic.raccoon",
            'name': "username",
            'id': 'username',
            'autocomplete': 'off'
        }
    ))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control form-control-lg form-control-solid',
            'placeholder': "example@example.com",
            'name': "email",
            'id': 'email',
            'autocomplete': 'off'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control form-control-lg form-control-solid",
            'placeholder': "strongPassword+151",
            'name': "password1",
            'id': 'password1',
            'autocomplete': 'off'
        }

    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control form-control-lg form-control-solid",
            'placeholder': "",
            'name': "password2",
            'id': 'password2',
            'autocomplete': 'off'
        }

    ))


    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        

        if password1 != password2:
            raise forms.ValidationError('Girilen telefon numaraları eşleşmiyor')

        values = {
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        }

        return values


