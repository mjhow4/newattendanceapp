from django.db import models

# Create your models here.
class Case(models.Model):
    no = models.CharField(max_length=4, null=True, blank=True)
    file_number = models.CharField(max_length=10, null=True, blank=True)
    defendant = models.CharField(max_length=50, null=True, blank=True)
    complainant = models.CharField(max_length=50, null=True, blank=True)
    offense = models.CharField(max_length=100, null=True, blank=True)
    attorney = models.CharField(max_length=50, null=True, blank=True)
    court_date = models.DateField(null=True, blank=True)
    plea_request = models.TextField(max_length=200, null=True, blank=True)
    response_by = models.TextField(max_length=200, null=True, blank=True)
    defense_name = models.CharField(max_length=50, null=True, blank=True)
    continuance = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name
