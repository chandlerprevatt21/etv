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