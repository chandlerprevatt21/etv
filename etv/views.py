from django.shortcuts import render, redirect

def home_page(request):
    context = {
    }
    return render(request, "home.html", context)

def about_page(request):
    context = {
    'title':'Coding Site | Learn to Code'
    }
    return render(request, "about.html", context)
