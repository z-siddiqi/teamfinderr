from django.db import models
from django.core.validators import  MaxValueValidator, MinValueValidator
from profiles.models import UserProfile
from django.contrib.auth import get_user_model
from enum import Enum

# Create your models here.
User = get_user_model()

class SkillType(models.Model):  # The type that the skill falls under -> e.g. python type is coding 
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.name}'
    
class Skill(models.Model): # table to store a skill -> skill is mapped to users and projects -> skill has a name, a type
    name = models.CharField(max_length=200)
    type = models.ForeignKey(SkillType,on_delete=models.CASCADE)
    # coding, business, etc

    def __str__(self):
        return f'{self.name}'
    
class Role(models.Model): # Role is the job role that a project requires  e.g. project manager, developer etc
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
    

# class Difficulty(models.Model):
#     pass # project difficulty (Used to determine candidates suitability)

class Project(models.Model): # a project that a user will create
    name = models.CharField(max_length=200) #charfield limited to 255 characters
    description = models.TextField(max_length=500) #Textfield >255 characters
    owner = models.ForeignKey(UserProfile, related_name='projects_owned', on_delete=models.CASCADE)
    members = models.ManyToManyField(UserProfile, through="ProjectMembership") #related_name makes it easier to query e.g. profile.projects
    #max_members = models.PositiveIntegerField() # the maximum number of people that a project can have (user defined and varies between projects)
    skills = models.ManyToManyField(Skill)
    #roles_req = models.ManyToManyField(Role)
    #difficulty = models.PositiveIntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.members.exists(): # only run when project is created
            member, created = ProjectMembership.objects.get_or_create(user=self.owner, project=self,invite_reason="Owner") # creates a ProjectMembership object with the project owner
            member.save()
            self.members.add(self.owner)
        return self
    
    def __str__(self):
        return f'{self.name}'
        
class ProjectMembership(models.Model):
    user = models.ForeignKey(UserProfile, related_name="project_memberships", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="project_memberships", on_delete=models.CASCADE)
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.user}{self.project}'


# make request model
# allow any member to accept requests
# each project has requests


class ProjectMembershipRequest(models.Model):
    from_user = models.ForeignKey(UserProfile, related_name='requests', on_delete=models.CASCADE)
    to_project = models.ForeignKey(Project, related_name='requests', on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=(("accepted", "Accepted"), ("pending", "Pending"), ("declined", "Declined")), default="pending")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == "accepted": 
            member, created = ProjectMembership.objects.get_or_create(user=self.from_user, 
                                                                        project=self.to_project,
                                                                        invite_reason="Role") # creates a ProjectMembership object with the from_user property
            member.save() 
            self.to_project.members.add(self.from_user)
            self.delete()

        elif self.status == "declined":
            self.delete()

        #return self

    

    def __str__(self):
        return f'{self.from_user} to {self.to_project}'

 
    