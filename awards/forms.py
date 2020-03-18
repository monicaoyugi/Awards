from django import forms
from . models import Profile, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email adress.')
    class Meta:
        model = User
        fields= ('username','email', 'password1','password2')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','user_name','bio')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['sitename','image','description','url']
