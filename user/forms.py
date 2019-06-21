from django.forms import models
from .models import UserData

class ProfilePicterEdit(models.ModelForm):
    class Meta:
        model = UserData
        fields = ['profilePicture']

class DescriptionEdit(models.ModelForm):
    class Meta:
        model = UserData
        fields = ['description']
        labels = {
            'description': ('')
        }