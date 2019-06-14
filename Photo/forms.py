from django import forms
from .models import Coments,Photo

class addComment(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['comment']


class AddPhoto(forms.ModelForm):
    class Meta:
        model=Photo
        fields = ['image','description']