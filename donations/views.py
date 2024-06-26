from http.client import HTTPResponse
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from donors.forms import DonorForm
from donors.models import Donor
from billing.models import BillingProfile
from addresses.models import Address
from addresses.forms import BillingAddressForm
from .models import donation
from django.core.mail import send_mail

from mailchimp_marketing import Client

mailchimp = Client()
mailchimp.set_config({
    "api_key": settings.MAILCHIMP_API_KEY,
    "server": "us7"
})
User = settings.AUTH_USER_MODEL
gateway = settings.GATEWAY

def receipt_generator(request):
    return render(request, 'email_test.html')

def update_donors(request):
    donors = Donor.objects.all()
    for x in donors:
        x.save()
    return HTTPResponse('success')
    
def send_test_email(request):
    send_mail(
        'Test!',
        'A successful test email has been sent',
        'admin@empowerthevillage.org',
        ['chandler@eliftcreations.com'],
        fail_silently=False
    )
    return HttpResponse('mail sent')

def mail_test(request):
    context = {
        'title': 'Send Mail Test'
    }
    return render(request, 'email_test.html', context)

def donate(request):
    tokenization_key = settings.BRAINTREE_TOKENIZATION_KEY
    donor_form = DonorForm()
    billing_address_form = BillingAddressForm()
    billing_addresses = None
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if billing_profile is not None:
        if request.user.is_authenticated:
            address_qs = Address.objects.filter(billing_profile=billing_profile)
            billing_addresses = address_qs.filter(address_type='billing')
    
    context = {
        'title': 'ETV | Donate',
        'mailing_form': donor_form,
        'billing_form': billing_address_form,
        'billing_addresses': billing_addresses,
        'tokenization_key': tokenization_key,
    }
    return render(request, "donate.html", context)

def donation_create(request):
    amount = request.POST.get('amount')
    frequency = request.POST.get('frequency')
    donor_level = request.POST.get('amount')
    first_name = request.POST.get('donor_first')
    last_name = request.POST.get('donor_last')
    phone = request.POST.get('donor_phone')
    email = request.POST.get('donor_email')
    request.session['guest_email'] = email
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    mailing_address, created = Address.objects.get_or_create(
        billing_profile = billing_profile,
        address_type = 'mailing',
        name = request.POST.get('name'),
        address_line_1 = request.POST.get('mailing_1'),
        address_line_2 = request.POST.get('mailing_2'),
        city = request.POST.get('mailing_city'),
        state = request.POST.get('mailing_state'),
        zip_code = request.POST.get('mailing_zip'),
    )
    donation_obj = donation.objects.new(email=email)
    donor_obj, created = Donor.objects.new_or_get(request)
    donation_obj.status = 'incomplete'
    donation_obj.billing_profile = billing_profile
    donation_obj.first_name = first_name
    donation_obj.last_name = last_name
    donation_obj.amount = amount
    if frequency is not None:
        donation_obj.frequency = frequency
    else:
        donation_obj.frequency = 'once'
    donation_obj.save()
    donor_obj.donations.add(donation_obj)
    donor_obj.first_name = first_name
    donor_obj.last_name = last_name
    donor_obj.donor_level = donor_level
    if donor_obj.default_mailing_address is not None:
        if donor_obj.default_mailing_address == mailing_address:
            pass
        else:
            donor_obj.mailing_addresses.add(mailing_address)
    else:
        donor_obj.default_mailing_address = mailing_address
    if phone is not None:
        donor_obj.phone = phone
    donor_obj.save()
    request.session['braintree_id'] = billing_profile.customer_id
    request.session['donation_id'] = donation_obj.id
    
    return HttpResponse('Incomplete Donation Created')

def donation_review(request):
    
    nonce = request.POST.get('nonce')
    donation_id = request.session.get('donation_id')
    donation_obj = donation.objects.get(id=donation_id)
    donation_obj.payment_method = nonce
    donation_obj.save()
    
    nonce_obj = gateway.payment_method_nonce.find(nonce)
    data = {
        'details': nonce_obj.details,
    }
    return JsonResponse(data)

def express_review(request):
    amount = request.POST.get('contact_info[amount]')
    frequency = request.POST.get('contact_info[frequency]')
    donor_level = request.POST.get('contact_info[amount]')
    first_name = request.POST.get('contact_info[donor_first]')
    last_name = request.POST.get('contact_info[donor_last]')
    phone = request.POST.get('contact_info[donor_phone]')
    email = request.POST.get('contact_info[donor_email]')
    request.session['guest_email'] = email
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    mailing_address, created = Address.objects.get_or_create(
        billing_profile = billing_profile,
        address_type = 'mailing',
        name = request.POST.get('contact_info[name]'),
        address_line_1 = request.POST.get('contact_info[mailing_1]'),
        address_line_2 = request.POST.get('contact_info[mailing_2]'),
        city = request.POST.get('contact_info[mailing_city]'),
        state = request.POST.get('contact_info[mailing_state]'),
        zip_code = request.POST.get('contact_info[mailing_zip]'),
    )
    donation_obj = donation.objects.new(email=email)
    try:
        donor_obj, created = Donor.objects.new_or_get(request)
    except:
        donor_obj = Donor()
    donation_obj.status = 'incomplete'
    donation_obj.billing_profile = billing_profile
    donation_obj.first_name = first_name
    donation_obj.last_name = last_name
    donation_obj.amount = amount
    if frequency is not None:
        donation_obj.frequency = frequency
    else:
        donation_obj.frequency = 'once'
    donation_obj.save()
    donor_obj.donations.add(donation_obj)
    donor_obj.first_name = first_name
    donor_obj.last_name = last_name
    donor_obj.donor_level = donor_level
    if donor_obj.default_mailing_address is not None:
        if donor_obj.default_mailing_address == mailing_address:
            pass
        else:
            donor_obj.mailing_addresses.add(mailing_address)
    else:
        donor_obj.default_mailing_address = mailing_address
    if phone is not None:
        donor_obj.phone = phone
    donor_obj.save()
    request.session['braintree_id'] = billing_profile.customer_id
    request.session['donation_id'] = donation_obj.id
    nonce = request.POST.get('nonce')
    donation_id = request.session.get('donation_id')
    donation_obj = donation.objects.get(id=donation_id)
    donation_obj.payment_method = nonce
    donation_obj.save()

    return HttpResponse('Incomplete Donation Created')

def donation_complete(request):
    donation_id = request.session.get('donation_id')
    donation_obj = donation.objects.get(id=donation_id)
    braintree_id = request.session.get('braintree_id')
    nonce = donation_obj.payment_method
    amount = donation_obj.amount
    first_name = str(donation_obj.first_name)
    last_name = str(donation_obj.last_name)
    email = str(donation_obj.billing_profile)
    frequency = donation_obj.frequency
    if frequency == 'once':
        result = gateway.transaction.sale({
            "amount": amount,
            "customer_id": braintree_id,
            "payment_method_nonce": nonce,
            "custom_fields": {
                "memo": 'Donation - %s from %s %s' %(amount, first_name, last_name)
            },
            "options": {
                "submit_for_settlement": True,
            },
        })
        if result.is_success:
            donation_obj.status = 'complete'
            donation_obj.braintree_id = result.transaction.id
            donation_obj.save()
            first_name = donation_obj.first_name
            amount = donation_obj.amount
            merge_fields = {
                "FNAME": str(first_name),
                "ETVAMOUNT": str(amount)
            }
            mailchimp.lists.set_list_member("bfb104d810", email, {"email_address": email, "status_if_new": "subscribed", "merge_fields": merge_fields})
            mailchimp.customerJourneys.trigger(2794, 15013, {"email_address": str(email)})
            send_mail(
                'New Donation!',
                str('A new $'+ str(amount) +' donation has been received from '+ str(donation_obj.get_full_name) +' through www.empowerthevillage.org!'),
                'etvnotifications@gmail.com',
                ['admin@empowerthevillage.org', 'chandler@eliftcreations.com', 'ayo@empowerthevillage.org'],
                #['chandler@eliftcreations.com'],
                fail_silently=True
            )
            del request.session['donation_id']
            data = 'success'
        else:
            data = 'error'
        return HttpResponse(data)
    elif frequency == 'monthly':
        plan_id = request.POST.get('plan_id')
        vault_result = gateway.payment_method.create({
            "customer_id": braintree_id,
            "payment_method_nonce": nonce,
        })
        if vault_result.is_success:
            token = vault_result.payment_method.token
            result = gateway.subscription.create({
            "payment_method_token": token,
            "plan_id": plan_id
            })
            if result.is_success:
                donation_obj.status = 'complete'
                donation_obj.payment_method = token
                donation_obj.subscription_id = result.subscription.id
                donation_obj.braintree_id = ''
                donation_obj.save()
                first_name = donation_obj.first_name
                amount = donation_obj.amount
                merge_fields = {
                    "FNAME": str(first_name),
                    "ETVAMOUNT": str(amount)
                }
                mailchimp.lists.set_list_member("bfb104d810", email, {"email_address": email, "status_if_new": "subscribed", "merge_fields": merge_fields})
                mailchimp.customerJourneys.trigger(2794, 15013, {"email_address": str(email)})
                send_mail(
                    'New Donation!',
                    str('A new recurring $'+ str(amount) +' donation has been received from '+ donation_obj.get_full_name +' through www.empowerthevillage.org!'),
                    'etvnotifications@gmail.com',
                    ['admin@empowerthevillage.org', 'chandler@eliftcreations.com', 'ayo@empowerthevillage.org'],
                    #['chandler@eliftcreations.com'],
                    fail_silently=True
                )
                data = 'success'
        else:
            data = 'error'
        return HttpResponse(data)
    else:
        result = gateway.transaction.sale({
            "amount": amount,
            "customer_id": braintree_id,
            "payment_method_nonce": nonce,
            "custom_fields": {
                "memo": 'donation'
            },
            "options": {
                "submit_for_settlement": True,
            },
        })
        if result.is_success:
            donation_obj.status = 'complete'
            donation_obj.frequency = 'once'
            donation_obj.braintree_id = result.transaction.id
            donation_obj.save()
            send_mail(
                'New Donation!',
                str('A new $'+ str(amount) +'donation has been received from '+ str(donation_obj.get_full_name) +'through www.empowerthevillage.org!'),
                'etvnotifications@gmail.com',
                ['admin@empowerthevillage.org', 'chandler@eliftcreations.com', 'ayo@empowerthevillage.org'],
                #['chandler@eliftcreations.com'],
                fail_silently=True
            )
            del request.session['donation_id']
            data = 'success'
        else:
            data = 'error'
        return HttpResponse(data)

def donation_analytics(request):
    donation_qs = donation.objects.all()
    context = {
        'title': 'Donation Analytics | ETV',
        'donations': donation_qs,

    }
    return render(request, "donation_analytics.html", context)


