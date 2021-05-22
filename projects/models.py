from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class CompletedProjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_date__lt=timezone.now())


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    members = models.ManyToManyField(User, through="ProjectMembership")
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)
    objects = models.Manager()  # default manager
    completed_objects = CompletedProjectsManager()  # custom completed projects manager

    def __str__(self):
        return self.name


class ProjectMembership(models.Model):
    user = models.ForeignKey(User, related_name="project_memberships", on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name="memberships", on_delete=models.CASCADE)
    role = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user} - {self.project}"


class ProjectMembershipRequest(models.Model):
    STATUS_CHOICES = (
        ("accepted", "Accepted"),
        ("pending", "Pending"),
        ("declined", "Declined"),
    )
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="pending")
    from_user = models.ForeignKey(User, related_name="sent_requests", on_delete=models.CASCADE)
    to_project = models.ForeignKey(Project, related_name="received_requests", on_delete=models.CASCADE)
    role = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.status == "accepted":
            ProjectMembership.objects.create(user=self.from_user, project=self.to_project, role=self.role)
        return self

    class Meta:
        unique_together = ("from_user", "to_project")

    def __str__(self):
        return f"{self.from_user} to {self.to_project}"
