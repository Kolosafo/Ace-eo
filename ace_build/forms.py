from django import forms
from django.forms import ModelForm, fields, widgets
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Optimization_form(ModelForm):
    class Meta:
        model = Optimization
        fields = ['title', 'description', 'tags', 'thumbnail']
        widgets = {
            'description' : forms.Textarea(
                attrs={
                    'oninput': 'strikeoff()',
                    "class": "form-control",
                    "cols": 30,
                    "rows": 10,
                    "label": "Description"
            
            } ),

             'title' : forms.TextInput (
                attrs={
                    "placeholder": "Enter title",
                    "class": "form-control",
                    "label": "Title"
            
            } ),

                'tags' : forms.TextInput (
            attrs={
                "placeholder": "write some tags",
                "class": "form-control",
                "label": "Tags",
                "required name": "tags",
                "value": "tags"  
        } )
        }   

class Keyword_Research_form(ModelForm):
    class Meta:
        model = Keyword_Research
        fields = ['keyword']
        widgets = {
            
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ThumbnailImageForm(ModelForm):
    class Meta:
        model = ThumbnailImage
        fields = ['image']