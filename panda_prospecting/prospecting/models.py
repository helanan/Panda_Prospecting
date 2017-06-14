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
        """Docstring goes here."""
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)


class Prospect(models.Model):
    """Adds a prospect model to our SQLite database."""

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    prospect_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """Returns a string of prospect text to interact with interface."""
        return self.prospect_text
