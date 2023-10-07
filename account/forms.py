from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'phonenumber')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'phonenumber')


class RegisterUserForm(forms.Form):
    phonenumber = PhoneNumberField(region='IR')
    password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('passwords is not same')
        return p2


class LoginForm(forms.Form):
    phonenumber = PhoneNumberField(region='IR')
    password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())


class RegisterUserFullForm(forms.ModelForm):
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ('date_joined','role','email')
        error_messages = {
            'phonenumber': {
                'invalid': 'شماره همراه نامعتبر است',
                'unique': 'کاربری با این شماره از قبل ثبت شده است'
            },
            # TODO: should add more error messages
        }

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
            raise forms.ValidationError('رمز های عبور وارد شده بایکدیگر مغایرت دارند ')
        return p2


class ResetPasswordSetForm(forms.Form):
    phonenumber = PhoneNumberField(region='IR')
    code = forms.CharField()
    password = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=64, min_length=8, required=True, widget=forms.PasswordInput())

    def clean_password2(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')
        if p1 != p2:
             raise forms.ValidationError('رمز های عبور وارد شده بایکدیگر مغایرت دارند ')
        return p2
