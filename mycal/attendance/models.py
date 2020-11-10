from django.db import models

# Create your models here.
class Case(models.Model):
    no = models.CharField(max_length=4,  null=True, blank=True)
    file_number = models.CharField(max_length=20,  null=True, blank=True)
    defendant_name = models.CharField(max_length=100,  null=True, blank=True)
    complainant = models.CharField(max_length=50, null=True, blank=True)
    offense = models.CharField(max_length=255,  null=True, blank=True)
    attorney = models.CharField(max_length=100,  null=True, blank=True)
    plea_request = models.CharField(max_length=400, null=True, blank=True)


    def __str__(self):
        return self.name