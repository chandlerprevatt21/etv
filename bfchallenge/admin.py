from django.contrib import admin
from .models import *
from accounts.admin import admin_site

admin.site.register(bingo_card)
admin.site.register(user_bingo_card)
admin_site.register(user_bingo_form)
admin_site.register(bingo_card)
admin_site.register(user_bingo_card)
admin_site.register(readysetshop_transaction)


