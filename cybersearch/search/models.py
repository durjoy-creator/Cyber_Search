from django.db import models

# Create your models here.

class searchcyber(models.Model):
    linkcyber  = models.CharField(max_length=255)
    titlecyber = models.CharField(max_length=255)
    descrcyber = models.TextField()

    def __str__(self):
        return self.titlecyber
