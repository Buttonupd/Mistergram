from django import forms
from .models import Comment, Image, Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['owner']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['image', 'comment-owner']
        
