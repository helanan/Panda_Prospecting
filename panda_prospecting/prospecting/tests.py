import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Account

# Create your tests here.
class AccountMethodTests(TestCase):
    def test_was_added_recently_with_future_account(self):
        """
        was_added_recently() should return False for questions whose date_added
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_account = Account(date_added=time)
        self.assertIs(future_account.was_added_recently(), False)

    def test_was_added_recently_with_old_account(self):
        """
        was_added_recently() should return False for questions whose
        added_date is older than a day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_account = Account(date_added=time)
        self.assertIs(old_account.was_added_recently(), False)

    def test_was_added_recently_with_recent_account(self):
        """
        was_added_recently() should run True for accounts whose added_date is
        within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_account = Account(date_added=time)
        self.assertIs(recent_account.was_added_recently(), True)
