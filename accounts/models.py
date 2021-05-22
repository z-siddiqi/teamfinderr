from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class SkillCategoryMixin(models.Model):
    CATEGORY_CHOICES = (
        ("relationship", "Relationship"),
        ("communication", "Communication"),
        ("management", "Management"),
        ("analytical", "Analytical"),
        ("creative", "Creative"),
        ("technical", "Technical"),
    )
    category = models.CharField(max_length=13, choices=CATEGORY_CHOICES)


class Skill(SkillCategoryMixin):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.category})"


class CustomUser(AbstractUser):
    bio = models.CharField(max_length=255, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="users")
