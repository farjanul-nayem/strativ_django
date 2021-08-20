from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SignupForm(forms.ModelForm):
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput, validators=[validate_password])
    password2 = forms.CharField(label='Password confirmation', required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist :
            return self.cleaned_data['username']
        raise forms.ValidationError("this username already exist")


    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
        except User.DoesNotExist :
            return self.cleaned_data['email']
        raise forms.ValidationError("this email already exist")


    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError("passwords dont match each other")
        return self.cleaned_data

    def save(self):
        user=User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password'])
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user