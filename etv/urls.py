"""etv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from accounts.admin import admin_site

from .views import home_page
from accounts.views import LoginView, RegisterView, GuestRegisterView
from vbp.views import home
from content.views import efbf, contact, mailchimp_signup

urlpatterns = [
    path('contact/', contact, name='contact' ),
    path('myadmin/etvadmin209423/', admin_site.urls, name='myadmin'),
    path('', efbf, name='home'),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include(("accounts.urls", "accounts"), namespace='account')),
    path('accounts/', include("accounts.passwords.urls")),
    path('black-friday-challenge/', include(("bfchallenge.urls", "bfchallenge"), namespace='bfchallenge')),
    path('donation/', include(("donations.urls", "donations"), namespace='donation')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOUGOUT_REDIRECT_URL), name='logout'),
    path('make-every-friday-black-friday/', efbf, name='efbf'),
    path('mailchimp-signup/', mailchimp_signup, name='mailchimp-signup'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/guest', GuestRegisterView.as_view(), name='guest_register'),
    path('settings/', RedirectView.as_view(url='/account')),
    path('village-black-pages/', include(("vbp.urls", "vbp"), namespace='vbp')),
    path('', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
