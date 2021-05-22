from django.contrib import admin
from .models import Project, ProjectMembership, ProjectMembershipRequest

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(ProjectMembershipRequest)
