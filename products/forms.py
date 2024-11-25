from django.forms import ModelForm
from django import forms

from . import models

class CommentsForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ('name', 'email', 'body')
