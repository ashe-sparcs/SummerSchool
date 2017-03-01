from django.db import models
import os


# Create your models here.
class Review(models.Model):
    number = models.IntegerField()
    student = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.TextField()


class Image(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    content = models.FileField(upload_to='media/image')

    def get_filename(self):
        return os.path.basename(self.content.name)


class ReviewImage(models.Model):
    content = models.FileField(upload_to='media/review_image')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def get_filename(self):
        return os.path.basename(self.content.name)


# class Schedule(models.Model):
#     academic_schedule = models.CharField(max_length=)
