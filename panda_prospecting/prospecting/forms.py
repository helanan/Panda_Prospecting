from django import forms

from .models import Account, Prospect

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_name', 'date_added', 'email', 'phone', 'street', 'city', 'state', 'zipcode', 'country', 'linkedin', 'account_status', 'account_notes']
        labels = {'account_name': 'Account Name', 'date_added': 'Date Added', 'email': 'General Email', 'phone': 'General Phone',
                  'street': 'Street', 'city': 'City', 'state': 'State', 'zipcode': 'Zipcode',
                  'country': 'Country', 'linkedin': 'LinkedIn', 'industry': 'Industry', 'account_status': 'Account Status', 'account_notes': 'Account Notes'}

class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = ['full_name', 'title', 'email', 'phone', 'street', 'city', 'state', 'zipcode', 'country', 'linkedin', 'prospect_status', 'prospect_notes', 'prospect_website']
        labels = {'full_name': 'Prospect Name', 'title': 'Title', 'email':'Email',
                  'phone':'Phone', 'street':'Street', 'city':'City', 'state':'State', 'zipcode':'ZipCode', 'country':'Country', 'linkedin':'LinkedIn', 'prospect_status': 'Prospect Status', 'prospect_notes': 'Prospect Notes', 'prospect_website': 'Prospect Website'}
        widgets = {'full_name': forms.Textarea(attrs={'cols': 80})}
