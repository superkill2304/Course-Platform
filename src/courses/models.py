from django.db import models


# Create your models here.

class AccessRequirement(models.TextChoices):

    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email required"

class PublishStatus(models.TextChoices):

    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"


class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    publish_date = models.DateField()
    access = models.CharField(max_length=25, choices=AccessRequirement.choices)

    status = models.CharField(
        max_length=5, choices=PublishStatus.choices, default=PublishStatus.DRAFT
    )

    @property
