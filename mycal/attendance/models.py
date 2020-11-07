from django.db import models

# Create your models here.
class Case(models.Model):
    case_number = models.CharField(max_length=255, null=True, blank=True)
    attorney = models.CharField(max_length=255,null=True, blank=True)
    court_session = models.CharField(max_length= 255,null=True, blank=True)
    plea_request = models.CharField (max_length= 255, null=True, blank=True)   

    def __str__(self):
        return self.attorney
