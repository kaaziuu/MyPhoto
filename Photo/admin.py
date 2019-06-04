from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Watching)
admin.site.register(Followed)
admin.site.register(Post)