from typing import Text
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import *
from vbp.models import *
from vbp.forms import NominationForm
from .forms import RSSForm, STLForm, EFForm
from content.forms import ContactForm
from content.models import contact_submission

import sweetify

def bingo(request):
    bingo = bingo_card.objects.all()
    contact_form = ContactForm()
    user = request.user
    user_bingo = None
    if user.is_authenticated:
        if user.is_bingo_sponsor or user.is_donor:
            user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    context = {
        'bingo_card': bingo,
        'user_bingo': user_bingo,
        'title': 'Power Bingo | ETV',
        'contact_form': contact_form
    }
    return render(request, "bingo.html", context)

def getTile1(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.save()
    user_bingo.spot1 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile3(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.save()
    user_bingo.spot3 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile4(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.save()
    user_bingo.spot4 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile5(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot5 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile6(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot6 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile7(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.field5 = request.POST['field5']
    formobj.field6 = request.POST['field6']
    formobj.save()
    user_bingo.spot7 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile8(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field1 = request.POST['field2']
    formobj.save()
    user_bingo.spot8 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile9(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot9 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile11(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot11 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile12(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.field5 = request.POST['field5']
    formobj.field6 = request.POST['field6']
    formobj.save()
    user_bingo.spot12 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile14(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field1 = request.POST['field2']
    formobj.save()
    user_bingo.spot14 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile15(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.field5 = request.POST['field5']
    formobj.field6 = request.POST['field6']
    formobj.field7 = request.POST['field7']
    formobj.field8 = request.POST['field8']
    formobj.field9 = request.POST['field9']
    formobj.field10 = request.POST['field10']
    formobj.field11 = request.POST['field11']
    formobj.field12 = request.POST['field12']
    formobj.save()
    user_bingo.spot15 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile17(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot17 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile18(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.field5 = request.POST['field5']
    formobj.save()
    user_bingo.spot18 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile19(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot19 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile20(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot20 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile21(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.save()
    user_bingo.spot21 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile22(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.save()
    user_bingo.spot22 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile23(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.field4 = request.POST['field4']
    formobj.field5 = request.POST['field5']
    formobj.field6 = request.POST['field6']
    formobj.save()
    user_bingo.spot23 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def getTile25(request):
  if request.method == 'POST':
    user = request.user
    user_bingo, created = user_bingo_card.objects.get_or_create(user=user)
    formobj = user_bingo_form()
    formobj.card = user_bingo
    formobj.spot = request.POST['spot']
    formobj.field1 = request.POST['field1']
    formobj.field2 = request.POST['field2']
    formobj.field3 = request.POST['field3']
    formobj.save()
    user_bingo.spot25 = True
    user_bingo.save()
    return HttpResponse('Thank you!')

def nomination_challenge(request):
    if request.method == 'POST':
        nomination_form = NominationForm(request.POST)
        if nomination_form.data['state'] == 'AL':
            obj = vbp_al()
        elif nomination_form.data['state'] == 'AZ':
            obj = vbp_az()
        elif nomination_form.data['state'] == 'AR':
            obj = vbp_ar()
        elif nomination_form.data['state'] == 'CA':
            obj = vbp_ca()
        elif nomination_form.data['state'] == 'CO':
            obj = vbp_co()
        elif nomination_form.data['state'] == 'CT':
            obj = vbp_ct()
        elif nomination_form.data['state'] == 'DE':
            obj = vbp_de()
        elif nomination_form.data['state'] == 'DC':
            obj = vbp_dc()
        elif nomination_form.data['state'] == 'FL':
            obj = vbp_fl()
        elif nomination_form.data['state'] == 'GA':
            obj = vbp_ga()
        elif nomination_form.data['state'] == 'HI':
            obj = vbp_hi()
        elif nomination_form.data['state'] == 'ID':
            obj = vbp_id()
        elif nomination_form.data['state'] == 'IL':
            obj = vbp_il()
        elif nomination_form.data['state'] == 'IN':
            obj = vbp_in()
        elif nomination_form.data['state'] == 'IA':
            obj = vbp_ia()
        elif nomination_form.data['state'] == 'KS':
            obj = vbp_ks()
        elif nomination_form.data['state'] == 'KY':
            obj = vbp_ky()
        elif nomination_form.data['state'] == 'LA':
            obj = vbp_la()
        elif nomination_form.data['state'] == 'ME':
            obj = vbp_me()
        elif nomination_form.data['state'] == 'MD':
            obj = vbp_md()
        elif nomination_form.data['state'] == 'MA':
            obj = vbp_ma()
        elif nomination_form.data['state'] == 'MI':
            obj = vbp_mi()
        elif nomination_form.data['state'] == 'MN':
            obj = vbp_mn()
        elif nomination_form.data['state'] == 'MS':
            obj = vbp_ms()
        elif nomination_form.data['state'] == 'MO':
            obj = vbp_mo()
        elif nomination_form.data['state'] == 'MT':
            obj = vbp_mt()
        elif nomination_form.data['state'] == 'NE':
            obj = vbp_ne()
        elif nomination_form.data['state'] == 'NV':
            obj = vbp_nv()
        elif nomination_form.data['state'] == 'NH':
            obj = vbp_nh()
        elif nomination_form.data['state'] == 'NJ':
            obj = vbp_nj()
        elif nomination_form.data['state'] == 'NM':
            obj = vbp_nm()
        elif nomination_form.data['state'] == 'NY':
            obj = vbp_ny()
        elif nomination_form.data['state'] == 'NC':
            obj = vbp_nc()
        elif nomination_form.data['state'] == 'ND':
            obj = vbp_nd()
        elif nomination_form.data['state'] == 'OH':
            obj = vbp_oh()
        elif nomination_form.data['state'] == 'OK':
            obj = vbp_ok()
        elif nomination_form.data['state'] == 'OR':
            obj = vbp_or()
        elif nomination_form.data['state'] == 'PA':
            obj = vbp_pa()
        elif nomination_form.data['state'] == 'RI':
            obj = vbp_ri()
        elif nomination_form.data['state'] == 'SC':
            obj = vbp_sc()
        elif nomination_form.data['state'] == 'SD':
            obj = vbp_sd()
        elif nomination_form.data['state'] == 'TN':
            obj = vbp_tn()
        elif nomination_form.data['state'] == 'TX':
            obj = vbp_tx()
        elif nomination_form.data['state'] == 'UT':
            obj = vbp_ut()
        elif nomination_form.data['state'] == 'VT':
            obj = vbp_vt()
        elif nomination_form.data['state'] == 'VA':
            obj = vbp_va()
        elif nomination_form.data['state'] == 'WA':
            obj = vbp_wa()
        elif nomination_form.data['state'] == 'WV':
            obj = vbp_wv()
        elif nomination_form.data['state'] == 'WI':
            obj = vbp_wi()
        elif nomination_form.data['state'] == 'WY':
            obj = vbp_wy()
        obj.business_name = nomination_form.data['business_name']
        obj.website = nomination_form.data['website']
        obj.city = nomination_form.data['city']
        obj.county = nomination_form.data['county']
        obj.phone = nomination_form.data['phone']
        obj.category = nomination_form.data['category']
        obj.subcategory = nomination_form.data['subcategory']
        obj.approved = 'False'
        if request.user.is_authenticated:
            obj.nominator_email = request.user.email
            obj.nominator_name = request.user.full_name
        else:
            obj.nominator_email = nomination_form.data['nominator_email']
            obj.nominator_name = nomination_form.data['nominator_name']
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for nominating a Black-owned business!', button='Nominate Another Business', timer=4000)
        obj.save()
        return redirect('/black-friday-challenge/nomination-challenge')
    else:
        nomination_form = NominationForm()
    context = {
        'title': 'VBP Nomination Challenge | ETV',
        'nomination_form': nomination_form
    }
    return render(request, 'nomination-challenge.html', context)

def ready_set_shop(request):
    if request.method == 'POST' and request.user.is_authenticated:
        rss_form = RSSForm(request.POST)
        obj = readysetshop_transaction()
        obj.user = request.user
        obj.business_name = rss_form.data['business_name']
        obj.amount = rss_form.data['amount']
        obj.date = rss_form.data['date']
        obj.industry = rss_form.data['industry']
        obj.receipt_aws = rss_form.data['receipt']
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for supporting a Black-owned business!', button='Add Another Transaction', timer=4000)
        obj.save()
        return redirect('/black-friday-challenge/ready-set-shop')
    elif request.method == 'POST':
        if request.method == 'POST':
            contact = ContactForm(request.POST)
            obj = contact_submission()
            obj.name = contact.data['name']
            obj.email = contact.data['email']
            obj.message = contact.data['message']
            if request.user.is_authenticated:
                user = request.user
                obj.user = user
            obj.save()
            sweetify.success(request, title='Thank you!', icon='success', text="We'll be in touch!", button='OK', timer=4000)
            return redirect('/black-friday-challenge/ready-set-shop')
    else:
        rss_form = RSSForm()
        contact_form = ContactForm()
    context = {
        'title': 'Ready, Set, Shop | ETV',
        'rss_form': rss_form,
        'contact_form': contact_form,
    }
    return render(request, 'ready-set-shop.html', context)

def everyfriday(request):
    if request.method == 'POST':
        rss_form = EFForm(request.POST)
        obj = everyfriday_transaction()
        obj.user = request.user
        obj.business_name = rss_form.data['business_name']
        obj.amount = rss_form.data['amount']
        obj.date = rss_form.data['date']
        obj.industry = rss_form.data['industry']
        obj.receipt_aws = rss_form.data['receipt']
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for supporting a Black-owned business!', button='Add Another Transaction', timer=4000)
        obj.save()
        return redirect('/black-friday-challenge/ready-set-shop')
    else:
        rss_form = RSSForm()
        contact_form = ContactForm()
    context = {
        'title': 'Ready, Set, Shop | ETV',
        'rss_form': rss_form,
        'contact_form': contact_form,
    }
    return render(request, 'every-friday.html', context)

def spread_the_love(request):
    if request.method == 'POST':
        stl_form = STLForm(request.POST)
        obj = spread_the_love_submission()
        obj.user = request.user
        obj.link = stl_form.data['link']
        
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for spreading the word!', timer=4000)
        obj.save()
        return redirect('/black-friday-challenge/spread-the-love')
    else:
        stl_form = STLForm()
    context = {
        'title': 'Spread The Love | ETV',
        'stl_form': stl_form,
    }
    return render(request, 'spread_the_love.html', context)
def bf_home(request):
    context = {
        'title': 'Black Friday Challenge | ETV'
    }
    return render(request, 'bf_home.html', context)