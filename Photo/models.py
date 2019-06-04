from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Watching(models.Model):
    watching = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    #status = 0 -> nobody follow
    #status = 1 -> smobody follow us
    #status = 2 -> followe each other


class Followed(models.Model):
    followed = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    #status = 0 -> nobodyfollow
    #status = 1 -> we follow somebody
    #status = 2 -> followe each other



class Post(models.Model):
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/',blank=False,null=False)
    slug = models.SlugField(blank=False,null=False,unique=True)

    def get_absolute_url(self):
        return f'/p/{self.slug}'
