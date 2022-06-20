from dataclasses import fields
from pyexpat import model
from django import forms
from .models import notes, userSignup

class usersignupForm(forms.ModelForm):
    class Meta:
        model=userSignup
        fields='__all__'


class notesForm(forms.ModelForm):
    class Meta:
        model=notes
        fields='__all__'