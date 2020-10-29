from django.db import models

# Create your models here.
class dataset(models.Model):
    name=models.CharField(max_length=100);
    calorie=models.CharField(max_length=100);

class users(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    tele=models.CharField(max_length=100);
    city=models.CharField(max_length=100);
    pwd=models.CharField(max_length=100);
    


