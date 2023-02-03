from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=50)
    calls = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'text')

    def __str__(self):
        return self.user.username + " | " + self.text
