from django.contrib import admin
from .models import Projects, Categories , Comment
# Register your models here.
admin.site.register(Projects)
admin.site.register(Categories)
admin.site.register(Comment)

