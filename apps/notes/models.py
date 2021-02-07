from django.db import models
from uuid import uuid4
from apps.users.models import User
# Create your models here.

class Note(models.Model):

    id = models.UUIDField(default=uuid4,
                        primary_key=True,
                        editable=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    stars = models.IntegerField(default=5)
    note = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return str(self.id)


