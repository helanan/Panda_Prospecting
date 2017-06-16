from django.contrib import admin

from .models import Prospect, Account

# Register your models here.
class ProspectInline(admin.TabularInline):
    model = Prospect
    extra = 3

class AccountAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['account_name']}),
        ('Date information', {'fields': ['date_added']}),
        ('Account General Email', {'fields': ['email']}),
        ('Account Telephone Information', {'fields': ['phone']}),
        ('Account Street Address', {'fields': ['street']}),
        ('Account City', {'fields': ['city']}),
        ('Account State', {'fields': ['state']}),
        ('Account Zipcode', {'fields': ['zipcode']}),
        ('Account Country', {'fields': ['country']}),
        ('Account LinkedIn', {'fields': ['linkedin']}),
        ('Account Status', {'fields': ['account_status']}),
        ('Account Notes', {'fields': ['account_notes']}),
        ]
    inlines = [ProspectInline]
    list_display = ('account_name', 'date_added', 'email', 'phone', 'street', 'city',
                    'state', 'zipcode', 'country', 'linkedin', 'account_status', 'account_notes',
                    'was_added_recently')
    list_filter = ['date_added']
    search_fields = ['account_name']


admin.site.register(Account, AccountAdmin)
