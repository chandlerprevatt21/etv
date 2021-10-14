from django.contrib import admin
from .models import *
from accounts.admin import admin_site

class RSSAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'amount', 'date', 'submitted']
    list_filter = ['team', 'industry']
    search_fields = ['user', 'team', 'amount', 'date', 'business_name', 'industry']
    ordering = ['team', 'submitted']
    

admin.site.register(bingo_card)
admin.site.register(user_bingo_card)
admin_site.register(user_bingo_form)
admin_site.register(bingo_card)
admin_site.register(user_bingo_card)
admin_site.register(readysetshop_transaction, RSSAdmin)


