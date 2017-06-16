from django import forms

from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name', 'date_added', 'email', 'phone', 'street', 'city', 'state', 'zipcode', 'country', 'linkedin', 'account_status', 'account_notes']
        labels = {'account_name': 'Account Name', 'date_added': 'Date Added', 'email': 'Account General Email', 'phone': 'General Phone', 'street': 'Street', 'city': 'City', 'state': 'State', 'zipcode': 'Zipcode',
                  'country': 'country', 'linkedin': 'linkedin', 'account_status': 'Account Status', 'account_notes': 'Account Notes'}
