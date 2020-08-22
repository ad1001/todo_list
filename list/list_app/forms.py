from django.forms import ModelForm
from django import forms
from .models import List

class TodoForm(ModelForm):
    text = forms.CharField(widget= forms.TextInput(
        attrs={
            "class":"validate",
            "placeholder":"New Task"
        }
    ))
    class Meta:
        model = List
        fields = ["text",]
      