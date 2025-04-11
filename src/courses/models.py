from django.db import models


# Create your models here.

class AccessRequirement(models.TextChoices):

    ANYONE = "any", "Anyone"
    EMAIL_REQUIRED = "email_required", "Email required"

class PublishStatus(models.TextChoices):

    PUBLISHED = "pub", "Published"
    COMING_SOON = "soon", "Coming Soon"
    DRAFT = "draft", "Draft"

def handle_upload(instance,filaname):
    return f"{filaname}"

class Course(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=handle_upload)
    publish_date = models.DateField()
    access = models.CharField(max_length=25, choices=AccessRequirement.choices, default= AccessRequirement.ANYONE)

    def __str__(self):
        return self.title

    status = models.CharField(
        max_length=5, choices=PublishStatus.choices, default=PublishStatus.DRAFT
    )

    @property 
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED