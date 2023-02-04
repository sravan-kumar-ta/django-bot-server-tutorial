from django.contrib.auth.models import User
from django.db import models


class Bot(models.Model):
    text = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    joke1 = models.TextField()
    joke2 = models.TextField()

    def __str__(self):
        return self.text


class BotCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE, related_name='bot_call')
    calls = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username + " | " + self.bot.text
