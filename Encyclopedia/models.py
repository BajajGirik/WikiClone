from django.db import models

# Create your models here.
class filenameloc(models.Model):
    title = models.CharField(max_length=64)
    path = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title}"
