from django import forms
from App.models import*

class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'