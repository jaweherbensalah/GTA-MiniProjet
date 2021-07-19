from django.db import models

# Create your models here.
class Formation(models.Model):
    titre =models.CharField(max_length=200)
    logo=models.CharField(max_length=300)
    etat =models.BooleanField()
    categorie=models.CharField(max_length=200)
    prix=models.FloatField()
    description=models.TextField()
