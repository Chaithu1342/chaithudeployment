from django.db import models
from django import forms
from django.contrib.auth.models import User
from chaithu_app.models import UserProfileInfo
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
from django import forms

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password'}))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype new password'}))

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        retype_password = cleaned_data.get('retype_password')

        if new_password != retype_password:
            raise forms.ValidationError("The passwords do not match.")
        return cleaned_data
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
# chaithu_app/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
# views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("chaithu_app:dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "chaithu_app/login.html", {"form": form})
