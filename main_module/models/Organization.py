from django.db import models
class Organization(models.Model):
    name= models.CharField(max_length=1024)
    ris_appetite= models.TextField(blank=True)
    ris_tolerance= models.TextField(blank=True)
    def __str__(self):
        return self.name
