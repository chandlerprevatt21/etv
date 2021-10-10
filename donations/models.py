from django.db import models

DONATION_LEVEL_CHOICES = (
    ('25', 'Village Member'),
    ('50', 'Village Patron'),
    ('100', 'Village Supporter'),
    ('500', 'Village Leader'),
    ('1000', 'Village Ambassador')
)
class donation_submission(models.Model):
    first_name      = models.CharField(max_length=50, unique=False)
    last_name       = models.CharField(max_length=50, unique=False)
    email           = models.EmailField(verbose_name='email address', max_length=255, unique=False,)
    donation_level  = models.CharField(max_length=100)
    recurring       = models.CharField(max_length=100, default='once')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'

class merch_order(models.Model):
    first_name      = models.CharField(max_length=50, unique=False)
    last_name       = models.CharField(max_length=50, unique=False)
    address_1       = models.CharField(max_length=400, unique=False)
    address_2       = models.CharField(max_length=400, unique=False)
    city            = models.CharField(max_length=200)
    state           = models.CharField(max_length=100)
    zip             = models.CharField(max_length=15)
    green_mugs            = models.IntegerField()
    white_mugs            = models.IntegerField()
    blackss_medium        = models.IntegerField()
    blackss_large         = models.IntegerField()
    blackss_xl            = models.IntegerField()
    blackss_xxl           = models.IntegerField()
    greyss_medium        = models.IntegerField()
    greyss_large         = models.IntegerField()
    greyss_xl            = models.IntegerField()
    greyss_xxl           = models.IntegerField()
    whitess_medium        = models.IntegerField()
    whitess_large         = models.IntegerField()
    whitess_xl            = models.IntegerField()
    whitess_xxl           = models.IntegerField()
    blackls_medium        = models.IntegerField()
    blackls_large         = models.IntegerField()
    blackls_xl            = models.IntegerField()
    blackls_xxl           = models.IntegerField()
    whitels_medium        = models.IntegerField()
    whitels_large         = models.IntegerField()
    whitels_xl            = models.IntegerField()
    whitels_xxl           = models.IntegerField()