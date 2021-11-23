from django.shortcuts import render, redirect
from .forms import BusinessForm
from .models import Nomination
import sweetify

def venForm(request):
    if request.method == 'POST':
        nomination_form = BusinessForm(request.POST)
        obj = Nomination()
        obj.business_name = nomination_form.data['business_name']
        obj.website = nomination_form.data['website']
        obj.city = nomination_form.data['city']
        obj.phone = nomination_form.data['phone']
        obj.category = nomination_form.data['category']
        obj.subcategory = nomination_form.data['subcategory']
        obj.save()
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for nominating a Black-owned business!', button='OK', timer=4000)
        return redirect('/village-empowerment-network-nomination')
    else:
        nomination_form = BusinessForm()
    return render(
        request, 
        'ven-form.html', 
        {
        'title': 'ETV | Village Empowerment Network Nomination Form',
        'nomination_form': nomination_form
        }
    )
