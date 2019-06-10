from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL
# Create your models here.


class FollowedStatus(models.Model):
    u1 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='u1')
    u2 = models.ForeignKey(User,on_delete=models.CASCADE,related_name='u2')
    status = models.IntegerField(default=0)
    #status = 0 -> nobodyfollow
    #status = 1 -> u1 follow u2
    #status = 2 -> u2 follow u1
    #status = 3 -> followe each other








class Photo(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='image/',blank=False,null=False)
    slug = models.SlugField(blank=False,null=False,unique=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    like = models.BigIntegerField(default=0)

    class Meta:
        ordering = ['-publish_date','-author']



    def get_absolute_url(self):
        return f'/p/{self.slug}'


class UserLike(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE)
    islike = models.BooleanField(default=True)


class Coments(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    photo = models.ForeignKey(Photo,on_delete=models.CASCADE,null=False)
    comment = models.TextField(null=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data','-author']