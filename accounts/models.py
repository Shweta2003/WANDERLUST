from django.db import models

# Create your models here.
class book(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    account=models.CharField(max_length=200)
    password=models.IntegerField()
    email=models.CharField(max_length=200)

class comment(models.Model):
    name=models.CharField(max_length=200)
    body=models.TextField()

