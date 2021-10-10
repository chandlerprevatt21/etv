import django
from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import vbp, vbp_book, vbp_al, vbp_az, vbp_az, vbp_ar, vbp_ca, vbp_co, vbp_ct, vbp_de, vbp_dc, vbp_fl, vbp_ga, vbp_hi, vbp_id, vbp_il, vbp_in, vbp_ia, vbp_ks, vbp_ky, vbp_la, vbp_me, vbp_md, vbp_ma, vbp_mi, vbp_mi, vbp_ms, vbp_mn, vbp_mo, vbp_mt, vbp_ne, vbp_nv, vbp_nh, vbp_nj, vbp_nm, vbp_ny, vbp_nc, vbp_nd, vbp_oh, vbp_ok, vbp_or, vbp_pa, vbp_ri, vbp_sc, vbp_sd, vbp_tn, vbp_tx, vbp_ut, vbp_vt, vbp_va, vbp_wa, vbp_wv, vbp_wi, vbp_wy  
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from .forms import NominationForm
from django.db.models import Count
from .models import StateFilter
import sweetify

import json
import django_filters
import geocoder

def get_counties_de(request):
    queryset = vbp_de.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", DE", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_ct(request):
    queryset = vbp_ct.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", CT", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_ny(request):
    queryset = vbp_ny.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", NY", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_nj(request):
    queryset = vbp_nj.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", NJ", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_ma(request):
    queryset = vbp_ma.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", MA", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_va(request):
    queryset = vbp_va.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", VA", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_oh(request):
    queryset = vbp_oh.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", OH", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_pa(request):
    queryset = vbp_pa.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", PA", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def get_counties_md(request):
    queryset = vbp_md.objects.all()
    for i in queryset:
        if not i.county:
            city = i.city
            geocode_result = geocoder.google(city+", MD", key='AIzaSyA1gqlqRGpMKsBiAKi9r0Q9b-v-BRDOL5k')
            county = geocode_result.current_result.county
            i.county = county
            i.save()
            print(i.county)
    return HttpResponse('Counties Got Got!')

def ct_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_ct.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_ct.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
            'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            })
        

def ny_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_ny.objects.all())
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_ny.objects.all()
    for object in filtered_qs:
        obj = object
        print(obj)
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
            'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def nj_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_nj.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_nj.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def ma_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_ma.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_ma.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def va_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_va.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_va.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def pa_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_pa.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_pa.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
            'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def oh_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_oh.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_oh.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
            'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def md_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_md.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_ct.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def dc_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_dc.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_dc.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def de_list(request):
    data = request.GET
    f = StateFilter(data, queryset=vbp_de.objects.order_by('city', 'business_name'))
    filtered_qs = f.qs
    beauty = filtered_qs.filter(category='beauty').order_by('city', 'business_name')
    books = filtered_qs.filter(category='books').order_by('city', 'business_name')
    cars = filtered_qs.filter(category='cars').order_by('city', 'business_name')
    child = filtered_qs.filter(category='child').order_by('city', 'business_name')
    cleaning = filtered_qs.filter(category='cleaning').order_by('city', 'business_name')
    clothing = filtered_qs.filter(category='clothing').order_by('city', 'business_name')
    construction = filtered_qs.filter(category='construction').order_by('city', 'business_name')
    education = filtered_qs.filter(category='education').order_by('city', 'business_name')
    eldercare = filtered_qs.filter(category='eldercare').order_by('city', 'business_name')
    electronics = filtered_qs.filter(category='electronics').order_by('city', 'business_name')
    entertainment = filtered_qs.filter(category='entertainment').order_by('city', 'business_name')
    farming = filtered_qs.filter(category='farming').order_by('city', 'business_name')
    florists = filtered_qs.filter(category='florists').order_by('city', 'business_name')
    grocery = filtered_qs.filter(category='grocery').order_by('city', 'business_name')
    health = filtered_qs.filter(category='health').order_by('city', 'business_name')
    home = filtered_qs.filter(category='home').order_by('city', 'business_name')
    hotels = filtered_qs.filter(category='hotels').order_by('city', 'business_name')
    jewelry = filtered_qs.filter(category='jewelry').order_by('city', 'business_name')
    legal = filtered_qs.filter(category='legal').order_by('city', 'business_name')
    lifestyle = filtered_qs.filter(category='lifestyle').order_by('city', 'business_name')
    marketing = filtered_qs.filter(category='marketing').order_by('city', 'business_name')
    medical = filtered_qs.filter(category='medical').order_by('city', 'business_name')
    other = filtered_qs.filter(category='other').order_by('city', 'business_name')
    packaging = filtered_qs.filter(category='packaging').order_by('city', 'business_name')
    pets = filtered_qs.filter(category='pets').order_by('city', 'business_name')
    photography = filtered_qs.filter(category='photography').order_by('city', 'business_name')
    professional = filtered_qs.filter(category='professional').order_by('city', 'business_name')
    realestate = filtered_qs.filter(category='real estate').order_by('city', 'business_name')
    recreation = filtered_qs.filter(category='recreation').order_by('city', 'business_name')
    restaurants = filtered_qs.filter(category='restaurants').order_by('city', 'business_name')
    security = filtered_qs.filter(category='security').order_by('city', 'business_name')
    transportation = filtered_qs.filter(category='transportation').order_by('city', 'business_name')
    visual = filtered_qs.filter(category='visual').order_by('city', 'business_name')

    paginator_beauty = Paginator(beauty, 22)
    beauty_page = 6
    paginator_books = Paginator(books, 22)
    books_page = beauty_page + paginator_beauty.num_pages + 1
    paginator_cars = Paginator(cars, 22)
    cars_page = books_page + paginator_books.num_pages + 1
    paginator_child = Paginator(child,22)
    child_page = cars_page + paginator_cars.num_pages + 1
    paginator_cleaning = Paginator(cleaning, 22)
    cleaning_page = child_page + paginator_child.num_pages + 1
    paginator_clothing = Paginator(clothing, 22)
    clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
    paginator_construction = Paginator(construction, 22)
    construction_page = clothing_page + paginator_clothing.num_pages + 1
    paginator_education = Paginator(education, 22)
    education_page = construction_page + paginator_construction.num_pages + 1
    paginator_eldercare = Paginator(eldercare, 22)
    eldercare_page = education_page + paginator_education.num_pages + 1
    paginator_electronics = Paginator(electronics, 22)
    electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
    paginator_entertainment = Paginator(entertainment, 22)
    entertainment_page = electronics_page + paginator_electronics.num_pages + 1
    paginator_farming = Paginator(farming, 22)
    farming_page = entertainment_page + paginator_entertainment.num_pages + 1
    paginator_florists = Paginator(florists, 22)
    florists_page = farming_page + paginator_farming.num_pages + 1
    paginator_grocery = Paginator(grocery, 22)
    grocery_page = florists_page + paginator_florists.num_pages + 1
    paginator_health = Paginator(health, 22)
    health_page = grocery_page + paginator_grocery.num_pages + 1
    paginator_home = Paginator(home, 22)
    home_page = health_page + paginator_health.num_pages + 1
    paginator_hotels = Paginator(hotels, 22)
    hotels_page = home_page + paginator_home.num_pages + 1
    paginator_jewelry = Paginator(jewelry, 22)
    jewelry_page = hotels_page + paginator_hotels.num_pages + 1
    paginator_legal = Paginator(legal, 22)
    legal_page = jewelry_page + paginator_jewelry.num_pages + 1
    paginator_lifestyle = Paginator(lifestyle, 22)
    lifestyle_page = legal_page + paginator_legal.num_pages + 1
    paginator_marketing = Paginator(marketing, 22)
    marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
    paginator_medical = Paginator(medical, 8)
    medical_page = marketing_page + paginator_marketing.num_pages + 1
    paginator_packaging = Paginator(packaging, 22)
    packaging_page = medical_page + paginator_medical.num_pages + 1
    paginator_pets = Paginator(pets, 22)
    pets_page = packaging_page + paginator_packaging.num_pages + 1
    paginator_photography = Paginator(photography, 22)
    photography_page = pets_page + paginator_pets.num_pages + 1
    paginator_professional = Paginator(professional, 22)
    professional_page = photography_page + paginator_photography.num_pages + 1
    paginator_realestate = Paginator(realestate, 22)
    realestate_page = professional_page + paginator_professional.num_pages + 1
    paginator_recreation = Paginator(recreation, 9)
    recreation_page = realestate_page + paginator_realestate.num_pages + 1
    paginator_restaurants = Paginator(restaurants, 22)
    restaurants_page = recreation_page + paginator_recreation.num_pages + 1
    paginator_security = Paginator(security, 22)
    security_page = restaurants_page + paginator_restaurants.num_pages + 1
    paginator_transportation = Paginator(transportation, 22)
    transportation_page = security_page + paginator_security.num_pages + 1
    paginator_visual = Paginator(visual, 22)
    visual_page = transportation_page + paginator_transportation.num_pages + 1
    paginator_other = Paginator(other, 22)
    other_page = visual_page + paginator_visual.num_pages + 1
    unfiltered_qs = vbp_de.objects.all()
    for object in filtered_qs:
        obj = object
        paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook_filtered.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'filtered_qs': filtered_qs,
                'unfiltered_qs': unfiltered_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )

def bookFilters(request):
    data = dict(request.GET)
    cities = request.GET.getlist('cities[]')
    categories = request.GET.getlist('categories[]')
    for city in cities:
        city_set = vbp_ct.objects.filter(city=city)
        for category in categories:
            category_set = city_set.objects.filter(category=category)
            print(category_set)
    return HttpResponse('success')

def home(request):
    f = StateFilter(request.GET, queryset=vbp_nj.objects.all())
    covers_qs = vbp_book.objects.all()
    initial_qs = vbp_ct.objects.all()
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
        obj.category = nomination_form.data['subcategory']
        obj.approved = 'False'
        obj.save()
        if request.user.is_authenticated:
            obj.nominator_email = request.user.email
            obj.nominator_name = request.user.full_name
        else:
            obj.nominator_email = nomination_form.data['nominator_email']
            obj.nominator_name = nomination_form.data['nominator_name']
        sweetify.success(request, title='Thank you!', icon='success', text='Thank you for nominating a Black-owned business!', button='Nominate Another Business', timer=4000)
        
        return redirect('/black-friday-challenge/nomination-challenge')
    else:
        nomination_form = NominationForm()
    return render(
        request, 
        'vbp_list.html', 
        {
        'covers_qs': covers_qs,
        'title': 'ETV | Village Black Pages',
        'initial_qs': initial_qs,
        'nomination_form': nomination_form,
        'filter': f}
    )

def getStateListings(request):
    state = request.GET['state']
    if state == 'US-AL':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_al.objects.all().order_by('city', 'business_name')),
        beauty = list(vbp_al.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_al.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_al.objects.filter(category='cars'))
        child = list(vbp_al.objects.filter(category='child'))
        cleaning = list(vbp_al.objects.filter(category='cleaning'))
        clothing = list(vbp_al.objects.filter(category='clothing'))
        construction = list(vbp_al.objects.filter(category='construction'))
        education = list(vbp_al.objects.filter(category='education'))
        eldercare = list(vbp_al.objects.filter(category='eldercare'))
        electronics = list(vbp_al.objects.filter(category='electronics'))
        entertainment = list(vbp_al.objects.filter(category='entertainment'))
        farming = list(vbp_al.objects.filter(category='farming'))
        florists = list(vbp_al.objects.filter(category='florists'))
        grocery = list(vbp_al.objects.filter(category='grocery'))
        health = list(vbp_al.objects.filter(category='health'))
        home = list(vbp_al.objects.filter(category='home'))
        hotels = list(vbp_al.objects.filter(category='hotels'))
        jewelry = list(vbp_al.objects.filter(category='jewelry'))
        legal = list(vbp_al.objects.filter(category='legal'))
        lifestyle = list(vbp_al.objects.filter(category='lifestyle'))
        marketing = list(vbp_al.objects.filter(category='marketing'))
        medical = list(vbp_al.objects.filter(category='medical'))
        other = list(vbp_al.objects.filter(category='other'))
        packaging = list(vbp_al.objects.filter(category='packaging'))
        pets = list(vbp_al.objects.filter(category='pets'))
        photography = list(vbp_al.objects.filter(category='photography'))
        professional = list(vbp_al.objects.filter(category='professional'))
        realestate = list(vbp_al.objects.filter(category='real estate'))
        recreation = list(vbp_al.objects.filter(category='recreation'))
        restaurants = list(vbp_al.objects.filter(category='restaurants'))
        security = list(vbp_al.objects.filter(category='security'))
        transportation = list(vbp_al.objects.filter(category='transportation'))
        visual = list(vbp_al.objects.filter(category='visual'))

        paginator_beauty = Paginator(beauty, 22)
        paginator_books = Paginator(books, 22)
        paginator_cars = Paginator(cars, 22)
        paginator_child = Paginator(child,22)
        paginator_cleaning = Paginator(cleaning, 22)
        paginator_clothing = Paginator(clothing, 22)
        paginator_construction = Paginator(construction, 22)
        paginator_education = Paginator(education, 22)
        paginator_eldercare = Paginator(eldercare, 22)
        paginator_electronics = Paginator(electronics, 22)
        paginator_entertainment = Paginator(entertainment, 22)
        paginator_farming = Paginator(farming, 22)
        paginator_florists = Paginator(florists, 22)
        paginator_grocery = Paginator(grocery, 22)
        paginator_health = Paginator(health, 22)
        paginator_home = Paginator(home, 22)
        paginator_hotels = Paginator(hotels, 22)
        paginator_jewelry = Paginator(jewelry, 22)
        paginator_legal = Paginator(legal, 22)
        paginator_lifestyle = Paginator(lifestyle, 22)
        paginator_marketing = Paginator(marketing, 22)
        paginator_medical = Paginator(medical, 22)
        paginator_other = Paginator(other, 22)
        paginator_packaging = Paginator(packaging, 22)
        paginator_pets = Paginator(pets, 22)
        paginator_photography = Paginator(photography, 22)
        paginator_professional = Paginator(professional, 22)
        paginator_realestate = Paginator(realestate, 22)
        paginator_recreation = Paginator(recreation, 22)
        paginator_restaurants = Paginator(restaurants, 22)
        paginator_security = Paginator(security, 22)
        paginator_transportation = Paginator(transportation, 22)
        paginator_visual = Paginator(visual, 22)
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-AZ':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_az.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_az.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_az.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_az.objects.filter(category='cars'))
        child = list(vbp_az.objects.filter(category='child'))
        cleaning = list(vbp_az.objects.filter(category='cleaning'))
        clothing = list(vbp_az.objects.filter(category='clothing'))
        construction = list(vbp_az.objects.filter(category='construction'))
        education = list(vbp_az.objects.filter(category='education'))
        eldercare = list(vbp_az.objects.filter(category='eldercare'))
        electronics = list(vbp_az.objects.filter(category='electronics'))
        entertainment = list(vbp_az.objects.filter(category='entertainment'))
        farming = list(vbp_az.objects.filter(category='farming'))
        florists = list(vbp_az.objects.filter(category='florists'))
        grocery = list(vbp_az.objects.filter(category='grocery'))
        health = list(vbp_az.objects.filter(category='health'))
        home = list(vbp_az.objects.filter(category='home'))
        hotels = list(vbp_az.objects.filter(category='hotels'))
        jewelry = list(vbp_az.objects.filter(category='jewelry'))
        legal = list(vbp_az.objects.filter(category='legal'))
        lifestyle = list(vbp_az.objects.filter(category='lifestyle'))
        marketing = list(vbp_az.objects.filter(category='marketing'))
        medical = list(vbp_az.objects.filter(category='medical'))
        other = list(vbp_az.objects.filter(category='other'))
        packaging = list(vbp_az.objects.filter(category='packaging'))
        pets = list(vbp_az.objects.filter(category='pets'))
        photography = list(vbp_az.objects.filter(category='photography'))
        professional = list(vbp_az.objects.filter(category='professional'))
        realestate = list(vbp_az.objects.filter(category='real estate'))
        recreation = list(vbp_az.objects.filter(category='recreation'))
        restaurants = list(vbp_az.objects.filter(category='restaurants'))
        security = list(vbp_az.objects.filter(category='security'))
        transportation = list(vbp_az.objects.filter(category='transportation'))
        visual = list(vbp_az.objects.filter(category='visual'))

        paginator_beauty = Paginator(beauty, 22)
        paginator_books = Paginator(books, 22)
        paginator_cars = Paginator(cars, 22)
        paginator_child = Paginator(child,22)
        paginator_cleaning = Paginator(cleaning, 22)
        paginator_clothing = Paginator(clothing, 22)
        paginator_construction = Paginator(construction, 22)
        paginator_education = Paginator(education, 22)
        paginator_eldercare = Paginator(eldercare, 22)
        paginator_electronics = Paginator(electronics, 22)
        paginator_entertainment = Paginator(entertainment, 22)
        paginator_farming = Paginator(farming, 22)
        paginator_florists = Paginator(florists, 22)
        paginator_grocery = Paginator(grocery, 22)
        paginator_health = Paginator(health, 22)
        paginator_home = Paginator(home, 22)
        paginator_hotels = Paginator(hotels, 22)
        paginator_jewelry = Paginator(jewelry, 22)
        paginator_legal = Paginator(legal, 22)
        paginator_lifestyle = Paginator(lifestyle, 22)
        paginator_marketing = Paginator(marketing, 22)
        paginator_medical = Paginator(medical, 22)
        paginator_other = Paginator(other, 22)
        paginator_packaging = Paginator(packaging, 22)
        paginator_pets = Paginator(pets, 22)
        paginator_photography = Paginator(photography, 22)
        paginator_professional = Paginator(professional, 22)
        paginator_realestate = Paginator(realestate, 22)
        paginator_recreation = Paginator(recreation, 22)
        paginator_restaurants = Paginator(restaurants, 22)
        paginator_security = Paginator(security, 22)
        paginator_transportation = Paginator(transportation, 22)
        paginator_visual = Paginator(visual, 22)
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-AR':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_ar.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_ar.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_ar.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_ar.objects.filter(category='cars'))
        child = list(vbp_ar.objects.filter(category='child'))
        cleaning = list(vbp_ar.objects.filter(category='cleaning'))
        clothing = list(vbp_ar.objects.filter(category='clothing'))
        construction = list(vbp_ar.objects.filter(category='construction'))
        education = list(vbp_ar.objects.filter(category='education'))
        eldercare = list(vbp_ar.objects.filter(category='eldercare'))
        electronics = list(vbp_ar.objects.filter(category='electronics'))
        entertainment = list(vbp_ar.objects.filter(category='entertainment'))
        farming = list(vbp_ar.objects.filter(category='farming'))
        florists = list(vbp_ar.objects.filter(category='florists'))
        grocery = list(vbp_ar.objects.filter(category='grocery'))
        health = list(vbp_ar.objects.filter(category='health'))
        home = list(vbp_ar.objects.filter(category='home'))
        hotels = list(vbp_ar.objects.filter(category='hotels'))
        jewelry = list(vbp_ar.objects.filter(category='jewelry'))
        legal = list(vbp_ar.objects.filter(category='legal'))
        lifestyle = list(vbp_ar.objects.filter(category='lifestyle'))
        marketing = list(vbp_ar.objects.filter(category='marketing'))
        medical = list(vbp_ar.objects.filter(category='medical'))
        other = list(vbp_ar.objects.filter(category='other'))
        packaging = list(vbp_ar.objects.filter(category='packaging'))
        pets = list(vbp_ar.objects.filter(category='pets'))
        photography = list(vbp_ar.objects.filter(category='photography'))
        professional = list(vbp_ar.objects.filter(category='professional'))
        realestate = list(vbp_ar.objects.filter(category='real estate'))
        recreation = list(vbp_ar.objects.filter(category='recreation'))
        restaurants = list(vbp_ar.objects.filter(category='restaurants'))
        security = list(vbp_ar.objects.filter(category='security'))
        transportation = list(vbp_ar.objects.filter(category='transportation'))
        visual = list(vbp_ar.objects.filter(category='visual'))

        paginator_beauty = Paginator(beauty, 22)
        paginator_books = Paginator(books, 22)
        paginator_cars = Paginator(cars, 22)
        paginator_child = Paginator(child,22)
        paginator_cleaning = Paginator(cleaning, 22)
        paginator_clothing = Paginator(clothing, 22)
        paginator_construction = Paginator(construction, 22)
        paginator_education = Paginator(education, 22)
        paginator_eldercare = Paginator(eldercare, 22)
        paginator_electronics = Paginator(electronics, 22)
        paginator_entertainment = Paginator(entertainment, 22)
        paginator_farming = Paginator(farming, 22)
        paginator_florists = Paginator(florists, 22)
        paginator_grocery = Paginator(grocery, 22)
        paginator_health = Paginator(health, 22)
        paginator_home = Paginator(home, 22)
        paginator_hotels = Paginator(hotels, 22)
        paginator_jewelry = Paginator(jewelry, 22)
        paginator_legal = Paginator(legal, 22)
        paginator_lifestyle = Paginator(lifestyle, 22)
        paginator_marketing = Paginator(marketing, 22)
        paginator_medical = Paginator(medical, 22)
        paginator_other = Paginator(other, 22)
        paginator_packaging = Paginator(packaging, 22)
        paginator_pets = Paginator(pets, 22)
        paginator_photography = Paginator(photography, 22)
        paginator_professional = Paginator(professional, 22)
        paginator_realestate = Paginator(realestate, 22)
        paginator_recreation = Paginator(recreation, 22)
        paginator_restaurants = Paginator(restaurants, 22)
        paginator_security = Paginator(security, 22)
        paginator_transportation = Paginator(transportation, 22)
        paginator_visual = Paginator(visual, 22)
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-CA':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_ca.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_ca.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_ca.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_ca.objects.filter(category='cars'))
        child = list(vbp_ca.objects.filter(category='child'))
        cleaning = list(vbp_ca.objects.filter(category='cleaning'))
        clothing = list(vbp_ca.objects.filter(category='clothing'))
        construction = list(vbp_ca.objects.filter(category='construction'))
        education = list(vbp_ca.objects.filter(category='education'))
        eldercare = list(vbp_ca.objects.filter(category='eldercare'))
        electronics = list(vbp_ca.objects.filter(category='electronics'))
        entertainment = list(vbp_ca.objects.filter(category='entertainment'))
        farming = list(vbp_ca.objects.filter(category='farming'))
        florists = list(vbp_ca.objects.filter(category='florists'))
        grocery = list(vbp_ca.objects.filter(category='grocery'))
        health = list(vbp_ca.objects.filter(category='health'))
        home = list(vbp_ca.objects.filter(category='home'))
        hotels = list(vbp_ca.objects.filter(category='hotels'))
        jewelry = list(vbp_ca.objects.filter(category='jewelry'))
        legal = list(vbp_ca.objects.filter(category='legal'))
        lifestyle = list(vbp_ca.objects.filter(category='lifestyle'))
        marketing = list(vbp_ca.objects.filter(category='marketing'))
        medical = list(vbp_ca.objects.filter(category='medical'))
        other = list(vbp_ca.objects.filter(category='other'))
        packaging = list(vbp_ca.objects.filter(category='packaging'))
        pets = list(vbp_ca.objects.filter(category='pets'))
        photography = list(vbp_ca.objects.filter(category='photography'))
        professional = list(vbp_ca.objects.filter(category='professional'))
        realestate = list(vbp_ca.objects.filter(category='real estate'))
        recreation = list(vbp_ca.objects.filter(category='recreation'))
        restaurants = list(vbp_ca.objects.filter(category='restaurants'))
        security = list(vbp_ca.objects.filter(category='security'))
        transportation = list(vbp_ca.objects.filter(category='transportation'))
        visual = list(vbp_ca.objects.filter(category='visual'))

        paginator_beauty = Paginator(beauty, 22)
        paginator_books = Paginator(books, 22)
        paginator_cars = Paginator(cars, 22)
        paginator_child = Paginator(child,22)
        paginator_cleaning = Paginator(cleaning, 22)
        paginator_clothing = Paginator(clothing, 22)
        paginator_construction = Paginator(construction, 22)
        paginator_education = Paginator(education, 22)
        paginator_eldercare = Paginator(eldercare, 22)
        paginator_electronics = Paginator(electronics, 22)
        paginator_entertainment = Paginator(entertainment, 22)
        paginator_farming = Paginator(farming, 22)
        paginator_florists = Paginator(florists, 22)
        paginator_grocery = Paginator(grocery, 22)
        paginator_health = Paginator(health, 22)
        paginator_home = Paginator(home, 22)
        paginator_hotels = Paginator(hotels, 22)
        paginator_jewelry = Paginator(jewelry, 22)
        paginator_legal = Paginator(legal, 22)
        paginator_lifestyle = Paginator(lifestyle, 22)
        paginator_marketing = Paginator(marketing, 22)
        paginator_medical = Paginator(medical, 22)
        paginator_other = Paginator(other, 22)
        paginator_packaging = Paginator(packaging, 22)
        paginator_pets = Paginator(pets, 22)
        paginator_photography = Paginator(photography, 22)
        paginator_professional = Paginator(professional, 22)
        paginator_realestate = Paginator(realestate, 22)
        paginator_recreation = Paginator(recreation, 22)
        paginator_restaurants = Paginator(restaurants, 22)
        paginator_security = Paginator(security, 22)
        paginator_transportation = Paginator(transportation, 22)
        paginator_visual = Paginator(visual, 22)
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-CO':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_co.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_co.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_co.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_co.objects.filter(category='cars'))
        child = list(vbp_co.objects.filter(category='child'))
        cleaning = list(vbp_co.objects.filter(category='cleaning'))
        clothing = list(vbp_co.objects.filter(category='clothing'))
        construction = list(vbp_co.objects.filter(category='construction'))
        education = list(vbp_co.objects.filter(category='education'))
        eldercare = list(vbp_co.objects.filter(category='eldercare'))
        electronics = list(vbp_co.objects.filter(category='electronics'))
        entertainment = list(vbp_co.objects.filter(category='entertainment'))
        farming = list(vbp_co.objects.filter(category='farming'))
        florists = list(vbp_co.objects.filter(category='florists'))
        grocery = list(vbp_co.objects.filter(category='grocery'))
        health = list(vbp_co.objects.filter(category='health'))
        home = list(vbp_co.objects.filter(category='home'))
        hotels = list(vbp_co.objects.filter(category='hotels'))
        jewelry = list(vbp_co.objects.filter(category='jewelry'))
        legal = list(vbp_co.objects.filter(category='legal'))
        lifestyle = list(vbp_co.objects.filter(category='lifestyle'))
        marketing = list(vbp_co.objects.filter(category='marketing'))
        medical = list(vbp_co.objects.filter(category='medical'))
        other = list(vbp_co.objects.filter(category='other'))
        packaging = list(vbp_co.objects.filter(category='packaging'))
        pets = list(vbp_co.objects.filter(category='pets'))
        photography = list(vbp_co.objects.filter(category='photography'))
        professional = list(vbp_co.objects.filter(category='professional'))
        realestate = list(vbp_co.objects.filter(category='real estate'))
        recreation = list(vbp_co.objects.filter(category='recreation'))
        restaurants = list(vbp_co.objects.filter(category='restaurants'))
        security = list(vbp_co.objects.filter(category='security'))
        transportation = list(vbp_co.objects.filter(category='transportation'))
        visual = list(vbp_co.objects.filter(category='visual'))

        paginator_beauty = Paginator(beauty, 22)
        paginator_books = Paginator(books, 22)
        paginator_cars = Paginator(cars, 22)
        paginator_child = Paginator(child,22)
        paginator_cleaning = Paginator(cleaning, 22)
        paginator_clothing = Paginator(clothing, 22)
        paginator_construction = Paginator(construction, 22)
        paginator_education = Paginator(education, 22)
        paginator_eldercare = Paginator(eldercare, 22)
        paginator_electronics = Paginator(electronics, 22)
        paginator_entertainment = Paginator(entertainment, 22)
        paginator_farming = Paginator(farming, 22)
        paginator_florists = Paginator(florists, 22)
        paginator_grocery = Paginator(grocery, 22)
        paginator_health = Paginator(health, 22)
        paginator_home = Paginator(home, 22)
        paginator_hotels = Paginator(hotels, 22)
        paginator_jewelry = Paginator(jewelry, 22)
        paginator_legal = Paginator(legal, 22)
        paginator_lifestyle = Paginator(lifestyle, 22)
        paginator_marketing = Paginator(marketing, 22)
        paginator_medical = Paginator(medical, 22)
        paginator_other = Paginator(other, 22)
        paginator_packaging = Paginator(packaging, 22)
        paginator_pets = Paginator(pets, 22)
        paginator_photography = Paginator(photography, 22)
        paginator_professional = Paginator(professional, 22)
        paginator_realestate = Paginator(realestate, 22)
        paginator_recreation = Paginator(recreation, 22)
        paginator_restaurants = Paginator(restaurants, 22)
        paginator_security = Paginator(security, 22)
        paginator_transportation = Paginator(transportation, 22)
        paginator_visual = Paginator(visual, 22)
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-CT':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_ct.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_ct.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_ct.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_ct.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_ct.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_ct.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_ct.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_ct.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_ct.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_ct.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_ct.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_ct.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_ct.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_ct.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_ct.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_ct.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_ct.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_ct.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_ct.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_ct.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_ct.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_ct.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_ct.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_ct.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_ct.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_ct.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_ct.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_ct.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_ct.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_ct.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_ct.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_ct.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_ct.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_ct.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_ct.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-DE':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_de.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_de.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_de.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_de.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_de.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_de.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_de.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_de.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_de.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_de.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_de.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_de.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_de.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_de.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_de.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_de.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_de.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_de.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_de.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_de.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_de.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_de.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_de.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_de.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_de.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_de.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_de.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_de.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_de.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_de.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_de.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_de.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_de.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_de.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_de.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-DC':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_dc.objects.all().order_by('category', 'city', 'business_name').ORDER_BY('CATEGORY', 'CITY', 'BUSINESS_NAME')),
        beauty = list(vbp_dc.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_dc.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_dc.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_dc.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_dc.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_dc.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_dc.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_dc.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_dc.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_dc.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_dc.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_dc.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_dc.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_dc.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_dc.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_dc.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_dc.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_dc.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_dc.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_dc.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_dc.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_dc.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_dc.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_dc.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_dc.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_dc.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_dc.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_dc.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_dc.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_dc.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_dc.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_dc.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_dc.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_dc.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-FL':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_fl.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-GA':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ga.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-HI':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_hi.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-ID':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_id.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-IL':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_il.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-IN':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_in.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-IA':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ia.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-KS':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ks.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-KY':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ky.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-LA':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_la.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-ME':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_me.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-MD':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_md.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_md.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_md.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_md.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_md.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_md.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_md.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_md.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_md.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_md.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_md.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_md.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_md.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_md.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_md.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_md.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_md.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_md.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_md.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_md.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_md.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_md.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_md.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_md.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_md.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_md.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_md.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_md.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_md.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_md.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_md.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_md.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_md.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_md.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_md.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-MA':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_ma.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_ma.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_ma.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_ma.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_ma.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_ma.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_ma.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_ma.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_ma.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_ma.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_ma.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_ma.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_ma.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_ma.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_ma.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_ma.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_ma.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_ma.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_ma.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_ma.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_ma.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_ma.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_ma.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_ma.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_ma.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_ma.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_ma.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_ma.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_ma.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_ma.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_ma.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_ma.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_ma.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_ma.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_ma.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-MI':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_mi.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-MS':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ms.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-MN':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_mn.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-MO':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_mo.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-MT':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_mt.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-NE':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ne.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-NV':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_nv.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-NH':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_nh.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-NJ':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_nj.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_nj.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_nj.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_nj.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_nj.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_nj.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_nj.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_nj.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_nj.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_nj.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_nj.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_nj.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_nj.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_nj.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_nj.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_nj.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_nj.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_nj.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_nj.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_nj.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_nj.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_nj.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_nj.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_nj.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_nj.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_nj.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_nj.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_nj.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_nj.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_nj.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_nj.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_nj.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_nj.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_nj.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_nj.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-NM':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_nm.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-NY':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_ny.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_ny.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_ny.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_ny.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_ny.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_ny.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_ny.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_ny.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_ny.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_ny.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_ny.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_ny.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_ny.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_ny.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_ny.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_ny.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_ny.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_ny.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_ny.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_ny.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_ny.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_ny.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_ny.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_ny.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_ny.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_ny.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_ny.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_ny.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_ny.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_ny.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_ny.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_ny.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_ny.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_ny.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_ny.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-NC':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_nc.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-ND':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_nd.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-OH':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_oh.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_oh.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_oh.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_oh.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_oh.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_oh.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_oh.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_oh.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_oh.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_oh.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_oh.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_oh.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_oh.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_oh.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_oh.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_oh.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_oh.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_oh.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_oh.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_oh.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_oh.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_oh.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_oh.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_oh.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_oh.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_oh.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_oh.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_oh.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_oh.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_oh.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_oh.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_oh.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_oh.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_oh.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_oh.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-OK':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ok.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-OR':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_or.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-PA':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_pa.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_pa.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_pa.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_pa.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_pa.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_pa.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_pa.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_pa.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_pa.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_pa.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_pa.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_pa.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_pa.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_pa.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_pa.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_pa.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_pa.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_pa.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_pa.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_pa.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_pa.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_pa.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_pa.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_pa.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_pa.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_pa.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_pa.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_pa.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_pa.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_pa.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_pa.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_pa.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_pa.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_pa.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_pa.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-RI':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ri.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-SC':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_sc.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-SD':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_sd.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-TN':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_tn.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-TX':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_tx.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-UT':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_ut.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-VT':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_vt.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-VA':
        covers_qs = vbp_book.objects.all()
        state_qs = list(vbp_va.objects.all().order_by('category', 'city', 'business_name')),
        beauty = list(vbp_va.objects.filter(category='beauty').order_by('city', 'business_name'))
        books = list(vbp_va.objects.filter(category='books').order_by('city', 'business_name'))
        cars = list(vbp_va.objects.filter(category='cars').order_by('city', 'business_name'))
        child = list(vbp_va.objects.filter(category='child').order_by('city', 'business_name'))
        cleaning = list(vbp_va.objects.filter(category='cleaning').order_by('city', 'business_name'))
        clothing = list(vbp_va.objects.filter(category='clothing').order_by('city', 'business_name'))
        construction = list(vbp_va.objects.filter(category='construction').order_by('city', 'business_name'))
        education = list(vbp_va.objects.filter(category='education').order_by('city', 'business_name'))
        eldercare = list(vbp_va.objects.filter(category='eldercare').order_by('city', 'business_name'))
        electronics = list(vbp_va.objects.filter(category='electronics').order_by('city', 'business_name'))
        entertainment = list(vbp_va.objects.filter(category='entertainment').order_by('city', 'business_name'))
        farming = list(vbp_va.objects.filter(category='farming').order_by('city', 'business_name'))
        florists = list(vbp_va.objects.filter(category='florists').order_by('city', 'business_name'))
        grocery = list(vbp_va.objects.filter(category='grocery').order_by('city', 'business_name'))
        health = list(vbp_va.objects.filter(category='health').order_by('city', 'business_name'))
        home = list(vbp_va.objects.filter(category='home').order_by('city', 'business_name'))
        hotels = list(vbp_va.objects.filter(category='hotels').order_by('city', 'business_name'))
        jewelry = list(vbp_va.objects.filter(category='jewelry').order_by('city', 'business_name'))
        legal = list(vbp_va.objects.filter(category='legal').order_by('city', 'business_name'))
        lifestyle = list(vbp_va.objects.filter(category='lifestyle').order_by('city', 'business_name'))
        marketing = list(vbp_va.objects.filter(category='marketing').order_by('city', 'business_name'))
        medical = list(vbp_va.objects.filter(category='medical').order_by('city', 'business_name'))
        other = list(vbp_va.objects.filter(category='other').order_by('city', 'business_name'))
        packaging = list(vbp_va.objects.filter(category='packaging').order_by('city', 'business_name'))
        pets = list(vbp_va.objects.filter(category='pets').order_by('city', 'business_name'))
        photography = list(vbp_va.objects.filter(category='photography').order_by('city', 'business_name'))
        professional = list(vbp_va.objects.filter(category='professional').order_by('city', 'business_name'))
        realestate = list(vbp_va.objects.filter(category='real estate').order_by('city', 'business_name'))
        recreation = list(vbp_va.objects.filter(category='recreation').order_by('city', 'business_name'))
        restaurants = list(vbp_va.objects.filter(category='restaurants').order_by('city', 'business_name'))
        security = list(vbp_va.objects.filter(category='security').order_by('city', 'business_name'))
        transportation = list(vbp_va.objects.filter(category='transportation').order_by('city', 'business_name'))
        visual = list(vbp_va.objects.filter(category='visual').order_by('city', 'business_name'))

        paginator_beauty = Paginator(beauty, 22)
        beauty_page = 6
        paginator_books = Paginator(books, 22)
        books_page = beauty_page + paginator_beauty.num_pages + 1
        paginator_cars = Paginator(cars, 22)
        cars_page = books_page + paginator_books.num_pages + 1
        paginator_child = Paginator(child,22)
        child_page = cars_page + paginator_cars.num_pages + 1
        paginator_cleaning = Paginator(cleaning, 22)
        cleaning_page = child_page + paginator_child.num_pages + 1
        paginator_clothing = Paginator(clothing, 22)
        clothing_page = cleaning_page + paginator_cleaning.num_pages + 1
        paginator_construction = Paginator(construction, 22)
        construction_page = clothing_page + paginator_clothing.num_pages + 1
        paginator_education = Paginator(education, 22)
        education_page = construction_page + paginator_construction.num_pages + 1
        paginator_eldercare = Paginator(eldercare, 22)
        eldercare_page = education_page + paginator_education.num_pages + 1
        paginator_electronics = Paginator(electronics, 22)
        electronics_page = eldercare_page + paginator_eldercare.num_pages + 1
        paginator_entertainment = Paginator(entertainment, 22)
        entertainment_page = electronics_page + paginator_electronics.num_pages + 1
        paginator_farming = Paginator(farming, 22)
        farming_page = entertainment_page + paginator_entertainment.num_pages + 1
        paginator_florists = Paginator(florists, 22)
        florists_page = farming_page + paginator_farming.num_pages + 1
        paginator_grocery = Paginator(grocery, 22)
        grocery_page = florists_page + paginator_florists.num_pages + 1
        paginator_health = Paginator(health, 22)
        health_page = grocery_page + paginator_grocery.num_pages + 1
        paginator_home = Paginator(home, 22)
        home_page = health_page + paginator_health.num_pages + 1
        paginator_hotels = Paginator(hotels, 22)
        hotels_page = home_page + paginator_home.num_pages + 1
        paginator_jewelry = Paginator(jewelry, 22)
        jewelry_page = hotels_page + paginator_hotels.num_pages + 1
        paginator_legal = Paginator(legal, 22)
        legal_page = jewelry_page + paginator_jewelry.num_pages + 1
        paginator_lifestyle = Paginator(lifestyle, 22)
        lifestyle_page = legal_page + paginator_legal.num_pages + 1
        paginator_marketing = Paginator(marketing, 22)
        marketing_page = lifestyle_page + paginator_lifestyle.num_pages + 1
        paginator_medical = Paginator(medical, 8)
        medical_page = marketing_page + paginator_marketing.num_pages + 1
        paginator_packaging = Paginator(packaging, 22)
        packaging_page = medical_page + paginator_medical.num_pages + 1
        paginator_pets = Paginator(pets, 22)
        pets_page = packaging_page + paginator_packaging.num_pages + 1
        paginator_photography = Paginator(photography, 22)
        photography_page = pets_page + paginator_pets.num_pages + 1
        paginator_professional = Paginator(professional, 22)
        professional_page = photography_page + paginator_photography.num_pages + 1
        paginator_realestate = Paginator(realestate, 22)
        realestate_page = professional_page + paginator_professional.num_pages + 1
        paginator_recreation = Paginator(recreation, 9)
        recreation_page = realestate_page + paginator_realestate.num_pages + 1
        paginator_restaurants = Paginator(restaurants, 22)
        restaurants_page = recreation_page + paginator_recreation.num_pages + 1
        paginator_security = Paginator(security, 22)
        security_page = restaurants_page + paginator_restaurants.num_pages + 1
        paginator_transportation = Paginator(transportation, 22)
        transportation_page = security_page + paginator_security.num_pages + 1
        paginator_visual = Paginator(visual, 22)
        visual_page = transportation_page + paginator_transportation.num_pages + 1
        paginator_other = Paginator(other, 22)
        other_page = visual_page + paginator_visual.num_pages + 1
        f = StateFilter(request.GET, queryset=vbp_va.objects.all())
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'beauty_page': beauty_page,
            'books_page': books_page,
            'cars_page': cars_page,
            'child_page': child_page,
            'cleaning_page': cleaning_page,
            'clothing_page': clothing_page,
            'construction_page': construction_page,
            'education_page': education_page,
            'eldercare_page': eldercare_page,
            'electronics_page': electronics_page,
            'entertainment_page': entertainment_page,
            'farming_page': farming_page,
            'florists_page': florists_page,
            'grocery_page': grocery_page,
            'health_page': health_page,
            'home_page': home_page,
            'hotels_page': hotels_page,
            'jewelry_page': jewelry_page,
            'legal_page': legal_page,
            'lifestyle_page': lifestyle_page,
            'marketing_page': marketing_page,
            'medical_page': medical_page,
            'packaging_page': packaging_page,
            'pets_page': pets_page,
            'photography_page': photography_page,
            'professional_page': professional_page,
            'realestate_page': realestate_page,
            'recreation_page': recreation_page,
            'restaurants_page': restaurants_page,
            'security_page': security_page,
            'transportation_page': transportation_page,
            'visual_page': visual_page,
            'other_page': other_page,
            'filter': f,
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'beauty': beauty,
            'paginator': paginator,
            'paginator_beauty': paginator_beauty,
            'paginator_books': paginator_books,
            'paginator_cars': paginator_cars,
            'paginator_child': paginator_child,
            'paginator_cleaning': paginator_cleaning,
            'paginator_clothing': paginator_clothing,
            'paginator_construction': paginator_construction,
            'paginator_education': paginator_education,
            'paginator_eldercare': paginator_eldercare,
            'paginator_electronics': paginator_electronics,
            'paginator_entertainment': paginator_entertainment,
            'paginator_farming': paginator_farming,
            'paginator_florists': paginator_florists,
            'paginator_grocery': paginator_grocery,
            'paginator_health': paginator_health,
            'paginator_home': paginator_home,
            'paginator_hotels': paginator_hotels,
            'paginator_jewelry': paginator_jewelry,
            'paginator_legal': paginator_legal,
            'paginator_lifestyle': paginator_lifestyle,
            'paginator_marketing': paginator_marketing,
            'paginator_medical': paginator_medical,
            'paginator_other': paginator_other,
            'paginator_packaging': paginator_packaging,
            'paginator_pets': paginator_pets,
            'paginator_photography': paginator_photography,
            'paginator_professional': paginator_professional,
            'paginator_realestate': paginator_realestate,
            'paginator_recreation': paginator_recreation,
            'paginator_restaurants': paginator_restaurants,
            'paginator_security': paginator_security,
            'paginator_transportation': paginator_transportation,
            'paginator_visual': paginator_visual,
            }
            )
    if state == 'US-WA':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_wa.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-WV':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_wv.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-WI':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_wi.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
    if state == 'US-WY':
        covers_qs = vbp_book.objects.all()
        state_qs = vbp_wy.objects.all().order_by('category', 'city', 'business_name'),
        for object in state_qs:
            obj = list(object)
            paginator = Paginator(obj, 22)
        return render(request, 
            'flipbook.html', 
            {
            'covers_qs': covers_qs,
            'state_qs': state_qs,
            'obj': obj,
            'paginator': paginator,
            }
            )
        
def filterList(request):
    get = request.GET
    
    print(get)
    items = get.items()
    print(items)
    return HttpResponse(220)
