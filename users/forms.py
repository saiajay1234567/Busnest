from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
# class userupdateform(forms.ModelForm):
#     email= forms.EmailField()
#     class meta:
#        model = User
#        fields=['username','email']
# class profileupdateform(forms.ModelForm):
   
#     image= forms.ImageField()
#     class meta:
#        model= Profile
#        fields=['image']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']