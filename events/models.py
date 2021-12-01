from datetime import date
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.http import HttpResponse
from django.urls import reverse
from etv.utils import unique_slug_generator

from ckeditor.fields import RichTextField

class tag(models.Model):
    tag             = models.CharField(max_length=270, blank=True, null=True)
    def __str__(self):
        return str(self.tag)

class Event(models.Model):
    title           = models.CharField(max_length=270)
    slug            = models.SlugField()
    details         = RichTextField()
    date            = models.DateTimeField(blank=True, null=True)
    tags            = models.ManyToManyField(tag, blank=True)

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"slug":self.slug})
    
    def __str__(self):
        return str(self.title)

def event_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(event_pre_save_receiver, sender=Event)