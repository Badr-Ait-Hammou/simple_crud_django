from django.db import models


# Create your models here.
class Patient(models.Model):
    nom = models.CharField(max_length=70)
    prenom = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    date = models.DateTimeField(max_length=100)
