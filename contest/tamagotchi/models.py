from django.db import models
from datetime import datetime, timedelta, timezone


class Pet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='pet',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='')
    fed = models.DateTimeField(auto_now_add=True)
    interacted = models.DateTimeField(auto_now_add=True)

    def hungry(self):
        """
        Determine if the pet has been fed in the last 6 hours or not.
        Why would you starve the kitty?  What's wrong with you?
        """
        now = datetime.now(timezone.utc)
        if now - self.fed > timedelta(hours=6):
            return True
        else:
            return False

    def bored(self):
        """
        Determine if the pet has been interacted with in the last 6 hours or not
        Don't you love your cat?  Meow?  Meow meow?
        Bored now.
        """
        now = datetime.now(timezone.utc)
        if now - self.interacted > timedelta(hours=6):
            return True
        else:
            return False

    class Meta:
        ordering = ['created']
