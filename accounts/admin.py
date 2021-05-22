from django.contrib import admin
from .models import CustomUser, Skill

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Skill)
