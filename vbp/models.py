from ctypes import addressof
import random
import os
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.db.models.fields import SlugField
from django.conf import settings
from accounts.models import Team
from phone_field import PhoneField

import geocoder
import django_filters
import json

User = settings.AUTH_USER_MODEL

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3000)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "vbp/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

STATE_CHOICES = [
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
]
CATEGORY_CHOICES = [
    ('beauty','Beauty & Personal Grooming'),
    ('books', 'Books & Publishing'),
    ('cars', 'Cars & Automotive'),
    ('child', "Childcare | Children's Services & Products"),
    ('cleaning', 'Cleaning'),
    ('clothing', 'Clothing & Fashion'),
    ('construction', 'Construction & Trades'),
    ('education', 'Education'),
    ('eldercare', 'Eldercare'),
    ('electronics', 'Electronics & Technology'),
    ('entertainment', 'Entertainment'),
    ('farming', 'Farming & Agriculture'),
    ('florists', 'Florists'),
    ('grocery', 'Grocery & Food Services'),
    ('health', 'Health & Wellness'),
    ('home', 'Home & Garden'),
    ('hotels', 'Hotels & Hospitality | Travel'),
    ('jewelry', 'Jewelry & Accessories'),
    ('legal', 'Legal & Financial Services'),
    ('lifestyle', 'Lifestyle'),
    ('marketing', 'Marketing & Advertising'),
    ('medical', 'Medical Services'),
    ('packaging', 'Packaging | Delivery | Shipping'),
    ('pets', 'Pets & Animal Care'),
    ('photography', 'Photography & Video'),
    ('professional', 'Professional Services'),
    ('real estate', 'Real Estate'),
    ('recreation', 'Recreation & Sports'),
    ('restaurants', 'Restaurants & Bars | Event Spaces'),
    ('security', 'Security Services'),
    ('transportation', 'Transportation & Trucking'),
    ('visual', 'Visual & Performing Arts | Culture'),
    ('other', 'Other'),
]

class vbpManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(approved=True)

class vbpStateManager(models.Manager):
    def filter_objs(self):
        filtered_qs = self
        return filtered_qs
        
    def dashboard_get_fields(self):
        list_fields = [{'field':'business_name','type':'plain'},{'field':'city','type':'plain'},{'field':'category','type':'plain'},{'field':'subcategory','type':'plain'},{'field':'approved','type':'plain'},]
        return list_fields
    
    def dashboard_get_view_fields(self):
        fields = [
            {'field':'business_name','type':'plain'},
            {'field':'category','type':'plain'}, 
            {'field':'subcategory','type':'plain'},
            {'field':'website','type':'url'},
            {'field':'phone','type':'plain'}, 
            {'field':'city','type':'plain'},
            {'field':'county','type':'plain'},

            {'field':'owner_name','type':'plain'},
            {'field':'owner_email','type':'email'},
            {'field':'nominator_name','type':'plain'},
            {'field':'nominator_email','type':'email'},
            
            {'field':'instagram','type':'instagram'},
            {'field':'facebook','type':'facebook'},
            {'field':'twitter','type':'twitter'},

            {'field':'approved','type':'boolean'},
        ]
        return fields
    
    def dashboard_display_qty(self):
        qty = 100
        return qty
        
    def dashboard_category(self):
        category = 'Village Black Pages'
        return category
    
    def get_grouping(self):
        grouping = "vbp_state"
        return grouping

class vbp(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, null=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    unapproved_objects = vbpManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'VBP Listing'
        verbose_name_plural = 'VBP Listings'

class vbpBookManager(models.Manager):
    def filter_objs(self):
        filtered_qs = self
        return filtered_qs
        
    def dashboard_get_fields(self):
        list_fields = [{'field':'state','type':'plain'},{'field':'published','type':'boolean'},]
        return list_fields
    
    def dashboard_get_view_fields(self):
        fields = [
            {'field':'state','type':'plain'},
            {'field':'cover','type':'img'}, 
            {'field':'published','type':'boolean'},
            {'field':'latitude','type':'coordinate'},
            {'field':'longitude','type':'coordinate'},
        ]
        return fields
    
    def dashboard_display_qty(self):
        qty = 52
        return qty
        
    def dashboard_category(self):
        category = 'Village Black Pages'
        return category

class vbp_book(models.Model):
    state           = models.CharField(max_length=50, choices=STATE_CHOICES)
    latitude        = models.CharField(max_length=200, blank=True, null=True)
    longitude       = models.CharField(max_length=200, blank=True, null=True)
    cover           = models.ImageField(null=True, blank=True)
    published       = models.BooleanField(default=False)
    featured        = models.BooleanField(default=False)
    
    objects         = vbpBookManager()
    
    def __str__(self):
        return str(self.state)
    
    @property
    def is_published(self):
        return self.is_published

    class Meta:
        verbose_name = 'VBP Book'
        verbose_name_plural = 'Books'
        ordering = ['-published', 'state']

class mv_private(models.Model):
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    owner_name       = models.CharField(max_length=300, blank=True, null=True)
    owner_email      = models.EmailField(blank=True, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    cat_ordering     = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.business_name)
    
    class Meta:
        ordering = ['category', 'cat_ordering', 'city', 'business_name']
        verbose_name = "Martha's Vineyard listing"
        verbose_name_plural = "Martha's Vineyard listings"
    
class vbp_al(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Alabama Listing'
        verbose_name_plural = 'Alabama Listings'

class vbp_ak(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Alaska Listing'
        verbose_name_plural = 'Alaska Listings'

class vbp_az(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Arizona Listing'
        verbose_name_plural = 'Arizona Listings'

class vbp_ar(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Arkansas Listing'
        verbose_name_plural = 'Arkansas Listings'

class vbp_ca(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=270)
    website          = models.URLField(blank=True, max_length=700, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=270, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'California Listing'
        verbose_name_plural = 'California Listings'

class vbp_co(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Colorado Listing'
        verbose_name_plural = 'Colorado Listings'

class vbp_ct(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False, blank=True, null=True)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, null=True, blank=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Connecticut Listing'
        verbose_name_plural = 'Connecticut Listings'

class vbp_de(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Delaware Listing'
        verbose_name_plural = 'Delaware Listings'

class vbp_dc(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'DC Listing'
        verbose_name_plural = 'DC Listings'

class vbp_fl(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Florida Listing'
        verbose_name_plural = 'Florida Listings'

class vbp_ga(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Georgia Listing'
        verbose_name_plural = 'Georgia Listings'

class vbp_hi(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Hawaii Listing'
        verbose_name_plural = 'Hawaii Listings'

class vbp_id(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Idaho Listing'
        verbose_name_plural = 'Idaho Listings'

class vbp_il(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Illinois Listing'
        verbose_name_plural = 'Illinois Listings'

class vbp_in(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Indiana Listing'
        verbose_name_plural = 'Indiana Listings'

class vbp_ia(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Iowa Listing'
        verbose_name_plural = 'Iowa Listings'

class vbp_ks(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Kansas Listing'
        verbose_name_plural = 'Kansas Listings'

class vbp_ky(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Kentucky Listing'
        verbose_name_plural = 'Kentucky Listings'

class vbp_la(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    address          = models.CharField(max_length=270, null=True, blank=True)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Louisiana Listing'
        verbose_name_plural = 'Louisiana Listings'

class vbp_me(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Maine Listing'
        verbose_name_plural = 'Maine Listings'

class vbp_md(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Maryland Listing'
        verbose_name_plural = 'Maryland Listings'

class vbp_ma(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Massachusetts Listing'
        verbose_name_plural = 'Massachusetts Listings'

class vbp_mi(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Michigan Listing'
        verbose_name_plural = 'Michigan Listings'

class vbp_mn(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Minnesota Listing'
        verbose_name_plural = 'Minnesota Listings'

class vbp_ms(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Mississippi Listing'
        verbose_name_plural = 'Mississippi Listings'

class vbp_mo(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Missouri Listing'
        verbose_name_plural = 'Missouri Listings'

class vbp_mt(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Montana Listing'
        verbose_name_plural = 'Montana Listings'

class vbp_ne(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Nebraska Listing'
        verbose_name_plural = 'Nebraska Listings'

class vbp_nv(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Nevada Listing'
        verbose_name_plural = 'Nevada Listings'

class vbp_nh(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'New Hampshire Listing'
        verbose_name_plural = 'New Hampshire Listings'

class vbp_nj(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False, null=True, blank=True)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True, blank=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, null=True, blank=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'New Jersey Listing'
        verbose_name_plural = 'New Jersey Listings'

class vbp_nm(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'New Mexico Listing'
        verbose_name_plural = 'New Mexico Listings'

class vbp_ny(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    approved         = models.BooleanField(default=False, null=True)
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'New York Listing'
        verbose_name_plural = 'New York Listings'


class vbp_nc(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'North Carolina Listing'
        verbose_name_plural = 'North Carolina Listings'

class vbp_nd(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'North Dakota Listing'
        verbose_name_plural = 'North Dakota Listings'

class vbp_oh(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Ohio Listing'
        verbose_name_plural = 'Ohio Listings'

class vbp_ok(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Oklahoma Listing'
        verbose_name_plural = 'Oklahoma Listings'

class vbp_or(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Oregon Listing'
        verbose_name_plural = 'Oregon Listings'

class vbp_pa(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)  
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)  
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Pennsylvania Listing'
        verbose_name_plural = 'Pennsylvania Listings'

class vbp_ri(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)   
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True) 
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Rhode Island Listing'
        verbose_name_plural = 'Rhode Island Listings'

class vbp_sc(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    address          = models.CharField(max_length=400, null=True, blank=True)
    zip_code         = models.CharField(max_length=100, null=True, blank=True)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)   
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True) 
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'South Carolina Listing'
        verbose_name_plural = 'South Carolina Listings'

class vbp_sd(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'South Dakota Listing'
        verbose_name_plural = 'South Dakota Listings'

class vbp_tn(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)   
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True) 
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Tennessee Listing'
        verbose_name_plural = 'Tennessee Listings'

class vbp_tx(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Texas Listing'
        verbose_name_plural = 'Texas Listings'

class vbp_ut(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)   
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True) 
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Utah Listing'
        verbose_name_plural = 'Utah Listings'

class vbp_vt(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Vermont Listing'
        verbose_name_plural = 'Vermont Listings'

class vbp_va(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Virginia Listing'
        verbose_name_plural = 'Virginia Listings'

class vbp_wa(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)    
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()
    
    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Washington Listing'
        verbose_name_plural = 'Washington Listings'

class vbp_wv(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)   
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True) 
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'West Virginia Listing'
        verbose_name_plural = 'West Virginia Listings'

class vbp_wi(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True)
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)    
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()

    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Wisconsin Listing'
        verbose_name_plural = 'Wisconsin Listings'

class vbp_wy(models.Model):
    directory_source  = models.CharField(max_length=200, null=True, blank=True)
    business_name    = models.CharField(max_length=200)
    website          = models.URLField(blank=True, max_length=500, null=True)
    instagram        = models.URLField(blank=True, null=True, max_length=200)
    twitter          = models.URLField(blank=True, null=True, max_length=200)
    facebook         = models.URLField(blank=True, null=True, max_length=200)
    city             = models.CharField(max_length=100, null=True, blank=True)
    county           = models.CharField(max_length=300, blank=True, null=True)
    phone            = PhoneField(blank=True, help_text='Business Phone Number')
    category         = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    subcategory      = models.CharField(max_length=200, blank=True, null=True)
    online_only      = models.BooleanField(default=False)
    nominator_name   = models.CharField(max_length=300, blank=True, null=True)
    nominator_email  = models.EmailField(blank=True, null=True) 
    nominator_owner  = models.BooleanField(default=False, blank=True, null=True)
    nominator_recommended  = models.BooleanField(default=False, blank=True, null=True)   
    owner_name   = models.CharField(max_length=300, blank=True, null=True)
    owner_email   = models.EmailField(blank=True, null=True)
    approved         = models.BooleanField(default=False, null=True)
    created          = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated          = models.DateTimeField(auto_now=True, blank=True, null=True)
    user             = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    team             = models.ForeignKey(Team, models.SET_NULL, null=True, blank=True)
    cat_ordering = models.IntegerField(blank=True, null=True)

    objects         = vbpStateManager()
    
    def __str__(self):
        return str(self.business_name)
    @property
    def is_approved(self):
         return self.approved

    class Meta:
        ordering = ['category', 'city', 'business_name']
        verbose_name = 'Wyoming Listing'
        verbose_name_plural = 'Wyoming Listings'

class StateFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(choices=CATEGORY_CHOICES)
    city = django_filters.CharFilter(max_length=255)
    county = django_filters.CharFilter(max_length=255)

