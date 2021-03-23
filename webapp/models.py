from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=100)
    pword=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.fname}'