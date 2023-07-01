from django.db import models

# Create your models here.
class Crystal(models.Model):
    name = models.CharField(max_length=500)
    img = models.CharField(max_length=500)
    bio = models.CharField(max_length=1000)
    location = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']