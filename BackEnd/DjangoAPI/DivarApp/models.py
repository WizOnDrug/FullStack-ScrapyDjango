from django.db import models

# Create your models here.
class Divar(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    construction_year = models.IntegerField()
    rooms = models.IntegerField()
    total_price = models.CharField(max_length=100)
    floor = models.IntegerField()
    elevator = models.CharField(max_length=100)
    parking = models.CharField(max_length=100)
    warehouse = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
