from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(FollowedStatus)
admin.site.register(Photo)
admin.site.register(UserLike)
admin.site.register(Coments)