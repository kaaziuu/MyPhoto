from django import forms
from .models import Coments

class addComment(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['comment']