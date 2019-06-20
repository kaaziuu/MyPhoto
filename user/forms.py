from django.forms import models
from .models import userData

class ProfilePicterEdit(models.ModelForm):
    class Meta:
        model = userData
        fields = ['profilePicture']

class DescriptionEdit(models.ModelForm):
    class Meta:
        model = userData
        fields = ['description']
        labels = {
            'description': ('')
        }