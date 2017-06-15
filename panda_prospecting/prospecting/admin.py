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
        ('Email information', {'fields': ['email']})
        ]
    inlines = [ProspectInline]
    list_display = ('account_name', 'date_added', 'email', 'was_added_recently')
    list_filter = ['date_added']
    search_fields = ['account_name']


admin.site.register(Account, AccountAdmin)
