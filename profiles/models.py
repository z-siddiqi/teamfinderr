from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class SkillCategoryMixin(models.Model):  # The type that the skill falls under -> e.g. python type is technical
    # the first element in each tuple is the actual value to be set on the
    # model, and the second element is the human-readable name
    CATEGORY_CHOICES = (
        ("relationship", "Relationship"),
        ("communication", "Communication"),
        ("management", "Management"),
        ("analytical", "Analytical"),
        ("creative", "Creative"),
        ("technical", "Technical"),
    )
    category = models.CharField(max_length=13, choices=CATEGORY_CHOICES)


class Skill(SkillCategoryMixin):  # table to store a skill -> skill is mapped to users and projects -> skill has a name, a category
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.category})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    skills = models.ManyToManyField(Skill, blank=True, related_name="profile")
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username