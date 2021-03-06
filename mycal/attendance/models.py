from django.db import models

# Create your models here.
class Case(models.Model):
    no = models.CharField(max_length=4, null=True, blank=True)
    file_number = models.CharField(max_length=10, null=True, blank=True)
    defendant = models.CharField(max_length=50, null=True, blank=True)
    complainant = models.CharField(max_length=50, null=True, blank=True)
    offense = models.CharField(max_length=100, null=True, blank=True)
    attorney = models.CharField(max_length=50, null=True, blank=True)
    plea_request = models.TextField(max_length=200, null=True, blank=True, default="---")
    response_by = models.TextField(max_length=200, null=True, blank=True, default="---")
    disposition = models.TextField(max_length=200, null=True, blank=True, default="---")
    defense_name = models.CharField(max_length=50, null=True, blank=True, default="---")
    continuance = models.CharField(max_length=12, null=True, blank=True, default="---")
    p = models.BooleanField(null=True, blank=True)
    a = models.BooleanField(null=True, blank=True)
    l = models.BooleanField(null=True, blank=True)
    cont_consent = models.CharField(max_length=12, null=True, blank=True, default="---")


    def __str__(self):
        return self.name
