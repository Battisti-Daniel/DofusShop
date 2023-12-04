import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account, Conjunto


class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm):
        model = Account
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Account.objects.filter(username=username).exists():
            raise forms.ValidationError('Already have a user with this username')
        if len(username) < 5:
            raise forms.ValidationError('Need have 5 or more characters')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 or not password2 or password1 != password2:
            raise forms.ValidationError('Password not match')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Account.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already in use')
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            raise forms.ValidationError(f"The email {email} doesn't seem valid")
        return email

class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email',]

    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    
