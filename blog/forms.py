from django import forms
from .models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    first_name = forms.CharField(help_text='Your First Name')
    last_name = forms.CharField(help_text='Your Last Name')
    username = forms.CharField(help_text='Username')
    password = forms.CharField(widget=forms.PasswordInput(), help_text='Password')
    email = forms.EmailField(max_length=50, help_text='Valid Email Address')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(required=False, help_text='Valid Website')
    profile_picture = forms.ImageField(help_text='Select a Profile Picture', required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'profile_picture', )
