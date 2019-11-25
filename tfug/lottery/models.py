from django.db import models

# Create your models here.
class Person(models.Model):
    personname=models.CharField(max_length=50)
    telephone=models.CharField(max_length=20)
    is_Lucky=models.IntegerField()  #1为中奖

class Result(models.Model):
    uid=models.IntegerField()
    personname=models.CharField(max_length=50)
    telephone=models.CharField(max_length=20)
    hours=models.IntegerField()