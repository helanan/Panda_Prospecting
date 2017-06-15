import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Account(models.Model):
    """Adds an account model to our SQLite database."""

    account_name = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    linkedin = models.URLField(max_length=30)
    account_status = models.CharField(max_length=30)
    account_notes = models.TextField

    def __str__(self):
        """Returns a string of account text to interact with interface."""
        return self.account_name

    def was_added_recently(self):
        """
        Returns boolean if an account was added by a user within a
        designated timeframe.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now
        was_added_recently.admin_order_field = 'date_added'
        was_added_recently.boolean = True
        was_added_recently.short_description = 'Added recently?'


class Prospect(models.Model):
    """Adds a prospect model to our SQLite database."""

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # prospect_photo = models.FileField(upload_to='uploads/%Y/%m/%d', height_field=None, width_field=None, max_length=100)
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=60)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    linkedin = models.URLField(max_length=30)
    prospect_status = models.CharField(max_length=30)
    prospect_notes = models.TextField
    prospect_views = models.IntegerField(default=0)

    def __str__(self):
        """Returns a string of prospect text to interact with interface."""
        return self.full_name
