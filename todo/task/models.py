# from datetime import datetime
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)
class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    # class Meta:
    #    ordering = ['-id']

class Note(models.Model):
    text = models.CharField(max_length=255)
    # created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.text


