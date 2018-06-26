from django.db import models
from django.contrib.auth.models import User

class Pack(models.Model):
    cod = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    cost = models.FloatField(default=0)
    cost_points = models.FloatField(default=0)

class SBC(models.Model):
    liga = models.CharField(max_length=200, default='')
    team = models.CharField(max_length=200)
    cod = models.IntegerField(default=0)
    valido = models.BooleanField(default=True)
    preco_ps4 = models.FloatField(default=0)
    preco_xone = models.FloatField(default=0)
    preco_pc = models.FloatField(default=0)
    pack = models.ForeignKey('Pack', on_delete=models.SET_NULL, null=True)

class SBC_FEITOS(models.Model):
    sbc = models.ForeignKey('SBC', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def as_dict(self):
        return {
            "id": self.sbc.id,
            "name":self.sbc.team,
        }

