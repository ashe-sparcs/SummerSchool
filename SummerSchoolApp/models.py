from django.db import models


# Create your models here.
class Review(models.Model):
    number = models.IntegerField()
    student = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.TextField()
