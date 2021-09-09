from django.urls import path
from django.conf.urls import url
from .views import donate

urlpatterns = [
    path('', donate, name='donate'),
]