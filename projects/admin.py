from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Role)
admin.site.register(models.ProjectMembership)
admin.site.register(models.ProjectMembershipRequest)
