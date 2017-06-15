import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Account

# Create your tests here.
class AccountMethodTests(TestCase):
    def test_was_added_recently_with_future_account(self):
        """
        was_added_recently() should return False for accounts whose date_added
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_account = Account(date_added=time)
        self.assertIs(future_account.was_added_recently(), False)

    def test_was_added_recently_with_old_account(self):
        """
        was_added_recently() should return False for accounts whose
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


def create_account(account_name, days):
    """
    Creates an account with the given `account_name` and published the given
    number of `days` offset to now (negative for accounts published in the
    past, positive for accounts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Account.objects.create(account_name=account_name, date_added=time)

class AccountViewTests(TestCase):
    def test_index_view_with_no_accounts(self):
        """
        If no accounts exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('prospecting:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No accounts have been added.")
        self.assertQuerysetEqual(response.context['latest_account_list'], [])

    def test_index_view_with_a_past_account(self):
        """
        Accounts with a date_added in the past should be displayed on the index
        page.
        """
        create_account(account_name="Past account.", days=-30)
        response = self.client.get(reverse('prospecting:index'))
        self.assertQuerysetEqual(
            response.context['latest_account_list'], ['<Account: Past account.>']
        )

    def test_index_view_with_a_future_account(self):
        """
        Accounts with a date_added in the future should not be displayed on the
        index page.
        """
        create_account(account_name="Future account.", days=30)
        response = self.client.get(reverse('prospecting:index'))
        self.assertContains(response, "No accounts have been added.")
        self.assertQuerysetEqual(response.context['latest_account_list'], [])

    def test_index_view_with_future_account_and_past_account(self):
        """Even if both past and future accounts exist, only past accounts
        should be displayed.
        """
        create_account(account_name="Past account.", days=-30)
        create_account(account_name="Future account.", days=30)
        response = self.client.get(reverse('polling:index'))
        self.assertQuerysetEqual(
            response.context['latest_account_list'], ['<Account: Past account.>']
        )
    def test_index_view_with_two_past_accounts(self):
        """
        The accounts index page may display multiple accounts.
        """
        create_account(account_name="Past account 1.", days=-30)
        create_account(account_name="Past account 2.", days=-5)
        response = self.client.get(reverse('prospecting:index'))
        self.assertQuerysetEqual(
            response.context['latest_account_list'], ['<Account: Past account 2.>', '<Account: Past account 1.>']
        )

class AccountIndexDetailTest(TestCase):
    def test_detail_view_with_a_future_account(self):
        """
        The detail view of an account with a date_added in the future should return
        a 404 not found.
        """
        future_account = create_account(account_name='Future account.', days=5)
        url = reverse('prospecting:detail', args=(future_account.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_account(self):
        """
        The detail view of an account with a date_added in the past should
        display the account's text.
        """
        past_account = create_account(account_name='Past Account.', days=-5)
        url = reverse('prospecting:detail', args=(past_account.id,))
        response = self.client.get(url)
        self.assertContains(response, past_account.account_name)
