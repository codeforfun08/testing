from django.db import models

# Create your models here.
class Book(models.Model):
    Name = models.CharField(max_length=30)
    Number = models.CharField(max_length=10)
    Email=models.CharField(max_length=30)
    Time=models.CharField(max_length=10)
    Subject=models.CharField(max_length=20)