from django.db import models
from uuid import uuid4

# Create your models here.
class Server(models.Model):
    id = models.UUIDField(default=uuid4,
                        primary_key=True,
                        editable=False)
    name = models.CharField(verbose_name='Server Name', max_length=20,unique=True)
    buyPrice = models.FloatField(verbose_name='Buying Price',default=0)
    sellPrice = models.FloatField(verbose_name='Selling Price',default=0)
    typesList = (
        ("MoC", "Mono-Compte"),
        ("MuC", "Multi-Compte"),
        ("Ret", "Retro"),
        ("MoRet", "Mono-Compte Retro"),
        ("Tch", "Touch")
    )
    serverType = models.CharField(verbose_name='Server Type' ,choices=typesList, max_length=255 ,default="Mono-Compte")
    stock = models.IntegerField(verbose_name='Kamas Stock')


    def __str__(self):
        return str(self.id)