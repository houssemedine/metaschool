from django.db import models

# Create your models here.
class Acadimic_year(models.Model):
    name=models.CharField(max_length=30,null=True)
    start=models.DateField()
    end=models.DateField()