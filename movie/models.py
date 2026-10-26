from django.db import models

# Create your models here.

class Category(models.Model):
    category=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.category


class Movie(models.Model):
    movie=models.CharField(max_length=100)
    trailer_link=models.URLField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    release_date=models.DateField()
    poster=models.ImageField(upload_to="poster/")
    description=models.TextField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)

    def __str__(self):
        return self.movie