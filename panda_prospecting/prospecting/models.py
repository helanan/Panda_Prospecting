import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    """Adds an account model to our SQLite database."""

    account_text = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')

    def __str__(self):
        """Returns a string of account text to interact with interface."""
        return self.account_text

    def was_added_recently(self):
        """
        Returns boolean if an account was added by a user within a
        designated timeframe.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now


class Prospect(models.Model):
    """Adds a prospect model to our SQLite database."""

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    prospect_text = models.CharField(max_length=200)
    prospect_views = models.IntegerField(default=0)

    def __str__(self):
        """Returns a string of prospect text to interact with interface."""
        return self.prospect_text
