from django.db import models
from uuid import uuid4
from apps.users.models import User
from apps.servers.models import Server
# Create your models here.

class Order(models.Model):
    id = models.UUIDField(default=uuid4,
                        primary_key=True,
                        editable=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    server = models.ForeignKey(Server, on_delete= models.CASCADE)
    orderTypes = (("sa","sale"),("pu","purchase"))
    orderType = models.CharField(choices=orderTypes, max_length=255)
    quantity = models.IntegerField(default=0)
    payChoice = models.CharField(max_length=255)
    amount = models.FloatField(default=0)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)