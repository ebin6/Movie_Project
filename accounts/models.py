from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    dob=models.DateField()
    profile_pic=models.ImageField(upload_to="users")
    place=models.CharField(max_length=30)