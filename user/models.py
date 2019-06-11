from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class userData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    profilePicture = models.ImageField(upload_to='image/profile/')
    description = models.TextField()