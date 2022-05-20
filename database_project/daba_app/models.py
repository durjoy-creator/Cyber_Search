from django.db import models

# Create your models here.
class Datasave(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    office = models.CharField(max_length=255)	
    age = models.CharField(max_length=2) 	
    start_date = models.CharField(max_length=255, blank=True) 	
    salary = models.CharField(max_length=255)

    def __str__(self):
        return self.name
