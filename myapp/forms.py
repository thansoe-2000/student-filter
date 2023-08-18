from django import forms
from .models import *
from django.forms import ModelForm

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"