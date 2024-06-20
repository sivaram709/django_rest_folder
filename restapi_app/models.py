from django.db import models

class student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    father=models.CharField(max_length=100)
    mother=models.CharField(max_length=100)

    def __str__(self):
        return self.name