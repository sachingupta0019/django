from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation

# User Registraion Form
class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    password2 = forms.CharField(label='Password(Enter again)', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(label='Email', required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username' : forms.TextInput(attrs={'class':'form-control'})}

## Login Form

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("password"),strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

# Password Change Form
class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "autofocus": True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New password"), strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

