from django.db import models

# Create your models here.
class Actors(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=40)
    about=models.TextField()
    dob=models.DateField()
    picture=models.ImageField(upload_to="actors/")