from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser): #inherits typical properties from AbstractUser ->  E.g. username, email etc
    def __str__(self):
        return f'{self.username}'
    


    
    
    
    

