from django.db import models
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Query(models.QuerySet):
    def search(self,query):
        lookup = (
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)|
            Q(user__username__icontains=query)
        )
        return self.filter(lookup)

    def by_nick(self,nick):
        lookup = (
            Q(user__username=nick)
        )
        return self.filter(lookup)

class UserMenager(models.Manager):
    def get_queryset(self):
        return Query(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)

    def by_nick(self,nick=None):
        if Query is None:
            return self.get_queryset().none()
        return self.get_queryset().by_nick(nick)







class userData(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    profilePicture = models.ImageField(upload_to='image/profile/',null=True,blank=True)
    description = models.TextField(null=True,blank=True)

    object = UserMenager()


