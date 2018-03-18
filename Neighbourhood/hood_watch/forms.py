from .models import User,Post
from django import forms
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = []
        widgets = {}
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = []
        widgets = {}
