from django.db import models

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['name']