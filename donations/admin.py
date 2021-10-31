from django.contrib import admin

from django.contrib import admin
from .models import donation_submission, donation
from accounts.admin import admin_site

class DonationAdmin(admin.ModelAdmin):
    list_display = ['amount', 'billing_profile', 'frequency', 'updated']
    list_filter = ['billing_profile', 'amount', 'frequency', 'status']
    search_fields = ['first_name', 'last_name', 'amount']
    ordering = ['-amount']
    
 
    
        
admin.site.register(donation_submission)
admin_site.register(donation, DonationAdmin)