from django.db import models

# Create your models here.
class Case(models.Model):
    no = models.CharField(max_length=4, null=True)
    file_number = models.CharField(max_length=10, null=True)
    defendant = models.CharField(max_length=50, null=True)
    complainant = models.CharField(max_length=50, null=True)
    offense = models.CharField(max_length=100, null=True)
    attorney = models.CharField(max_length=50, null=True)
    court_date = models.DateField(null=True)
    plea_request = models.TextField(max_length=200, null=True)
    response_by = models.TextField(max_length=200, null=True)


    def __str__(self):
        return self.name