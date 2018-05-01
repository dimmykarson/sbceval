from django.db import models


class Pack(models.Model):
    name = models.CharField(max_length=200)
    cost = models.FloatField()

# Create your models here.
class SBC(models.Model):
    team = models.CharField(max_length=200)
