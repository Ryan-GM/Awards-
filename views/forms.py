from django import forms
from .models import Post,Rating,Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = Post
        fields = ('photo', 'title', 'url', 'description', 'technologies',)