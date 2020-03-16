from django import forms
from . models import Project, Post

class SignUpForm(userCreatonForm):
    email = forms.EmailField(max_length=254, help_text='Required. Provide a valid email adress.')
    class Meta:
        model = User
        fields= ('username','email', 'password1','password2')

class ImageForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user']

class UsabilityForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['rating']

class UserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name','user_name','bio')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['sitename','image','description','url']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','image', 'date_posted']