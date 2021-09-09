from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import donation_submission
from accounts.admin import admin_site

admin.site.register(donation_submission)
admin_site.register(donation_submission)