from django.db import models

# Create your models here.
from django.db import models

class ReferenceProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    client = models.CharField(max_length=255, blank=True)
    value = models.CharField(max_length=50, blank=True)  # e.g. "€100M"
    location = models.CharField(max_length=255, blank=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
