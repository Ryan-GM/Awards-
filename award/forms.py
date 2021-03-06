from django import forms
from .models import Post,Rating,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from pyuploadcare.dj.models import ImageField

class PostForm(forms.ModelForm):
    # photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo',)

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'location', 'bio', 'contact']

class RatingsForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']