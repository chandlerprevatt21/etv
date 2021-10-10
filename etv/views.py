from django.shortcuts import render, redirect

def home_page(request):
    context = {
        'title':'ETV | Home'
    }
    return render(request, "home.html", context)

def about_page(request):
    context = {
    'title':'ETV | About'
    }
    return render(request, "about.html", context)

def strategic_pillars(request):
    context = {
    'title':'ETV | Strategic Pillars'
    }
    return render(request, "strategic-pillars.html", context)

def economic_prosperity(request):
    context = {
        'title': 'ETV | Economic Prosperity',
    }
    return render(request, "prosperity.html", context)

def news(request):
    context = {
    'title':'ETV | News & Events'
    }
    return render(request, "news.html", context)

def shop(request):
    context = {
        'title': 'ETV | Shop',
    }
    return render(request, "shop.html", context)
