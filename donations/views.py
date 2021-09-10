from django.shortcuts import render
from .forms import DonationForm
from .models import donation_submission
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings

import sweetify

def donate(request):
    donation_form = DonationForm()
    if request.method == 'POST':
        donation_form = request.POST
        print(donation_form)
        obj = donation_submission()
        obj.first_name = donation_form['first_name']
        obj.donation_level = donation_form['donation_level']
        obj.email  = donation_form['donor_email']
        obj.recurring = donation_form['recurring']
        if request.user.is_authenticated:
            user = request.user
            user.donor = True
            user.save()
        obj.save()
        sweetify.success(request, 'Thank You For Supporting Empower The Village!', text="You're now eligible to play Power Bingo and participate in the Every Friday Challenge!", persistent='', button='OK', html='', timer='25000', showCloseButton=True,)
        return redirect('/donation/')
    context = {
        'title': 'Donate | ETV',
        'donation_form': donation_form,
    }
    return render(request, "donate.html", context)
