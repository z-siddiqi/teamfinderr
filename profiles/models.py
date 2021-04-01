from django.db import models
from accounts.models import CustomUser 

# Create your models here.
class UserProfile(models.Model):
    profile = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
        
    def __str__(self):
        return f'{self.profile.username}'
