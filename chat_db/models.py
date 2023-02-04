from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BotCall(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stupid = models.PositiveIntegerField(default=0)
    fat = models.PositiveIntegerField(default=0)
    dump = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username
