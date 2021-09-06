from django import forms
from django.forms import fields, widgets
from .models import userdata1



class userform1(forms.ModelForm):
    class Meta:
        model=userdata1
        fields=['username','email','Address']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.TextInput(attrs={'class':'form-control'})
        }
