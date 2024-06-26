from django import forms
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.widgets import TextInput
from django.urls import reverse
from django.utils.safestring import mark_safe

User = get_user_model()

from vbp.models import vbp
from accounts.signals import user_logged_in

CATEGORY_CHOICES = (
    ('none', 'Choose A Category'),
    ('beauty','Beauty & Personal Grooming'),
    ('books', 'Books & Publishing'),
    ('cars', 'Cars & Automotive'),
    ('child', "Childcare | Children's Services & Products"),
    ('cleaning', 'Cleaning'),
    ('clothing', 'Clothing & Fashion'),
    ('construction', 'Construction & Trades'),
    ('education', 'Education'),
    ('eldercare', 'Eldercare'),
    ('electronics', 'Electronics & Technology'),
    ('entertainment', 'Entertainment'),
    ('farming', 'Farming & Agriculture'),
    ('florists', 'Florists'),
    ('grocery', 'Grocery & Food Services'),
    ('health', 'Health & Wellness'),
    ('home', 'Home & Garden'),
    ('hotels', 'Hotels & Hospitality | Travel'),
    ('jewelry', 'Jewelry & Accessories'),
    ('legal', 'Legal & Financial Services'),
    ('lifestyle', 'Lifestyle'),
    ('marketing', 'Marketing & Advertising'),
    ('medical', 'Medical Services'),
    ('packaging', 'Packaging | Delivery | Shipping'),
    ('pets', 'Pets & Animal Care'),
    ('photography', 'Photography & Video'),
    ('professional', 'Professional Services'),
    ('real estate', 'Real Estate'),
    ('recreation', 'Recreation & Sports'),
    ('restaurants', 'Restaurants & Bars | Event Spaces'),
    ('security', 'Security Services'),
    ('transportation', 'Transportation & Trucking'),
    ('visual', 'Visual & Performing Arts | Culture'),
    ('other', 'Other'),
)
STATE_CHOICES = (
    ('none', 'Select A State'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)
TRUEFALSE_CHOICES = (
    ('true', 'Yes'),
    ('false', 'No')
)

SUBCATEGORY_CHOICES = (
    ('none', 'Choose A Sub-Category'),
    ("barber", "Barber"),
    ("bathandbody", "Bath & Body"),
    ("beautysalon", "Beauty Salon"),
    ("beautysupply", "Beauty Supply/Hair & Accessories"),
    ("cosmetics", "Cosmetics"),
    ("nails", "Nails"),
    ("travelingstylist", "Traveling Stylist"),
    ("bookstore", "Book Store"),
    ("onlinepub", "Online Publication"),
    ("publishing", "Publishing"),
    ("authors", "Authors"),
    ("autodealership", "Auto Dealership"),
    ("autorepair", "Auto Repair/ Services"),
    ("carwash", "Car Wash"),
    ("gasstation", "Gas Station"),
    ("babyproducts", "Baby Products"),
    ("childcare", "Childcare/Daycare/ Preschool"),
    ("childbooks", "Children’s Books"),
    ("childactivities", "Children’s Activities"),
    ("cleaningproducts", "Cleaning Products"),
    ("drycleaning", "Dry Cleaning"),
    ("laundry", "Laundry"),
    ("apparel", "Apparel"),
    ("stylist", "Stylist"),
    ("footwear", "Footwear"),
    ("fabric", "Fabric/Yarn"),
    ("appliancerepair", "Appliance Repair"),
    ("construction", "Construction/ Engineering"),
    ("electrical", "Electrical"),
    ("hvac", "HVAC"),
    ("plumbing", "Plumbing"),
    ("powerwashing", "Power Washing"),
    ("roofing", "Roofing & Siding"),
    ("paintingservices", "Painting Services"),
    ("tutor", "Tutoring/ Academic Planning"),
    ("driving", "Driving/ Aviation"),
    ("enrichment", "Enrichment"),
    ("assistedliving", "Assisted Living/Nursing Home"),
    ("homehealth", "Home Health Care/ Nursing Services"),
    ("adultdaycare", "Adult Day Care Center"),
    ("cybersecurity", "Cybersecurity"),
    ("software", "Software Development"),
    ("techsupport", "Tech Support/ Repair"),
    ("techproducts", "Tech Products"),
    ("webservices", "Web Services"),
    ("bands", "Bands/DJs/Performers"),
    ("comedian", "Comedian"),
    ("eventplanning", "Event Planning/Services"),
    ("media", "Media"),
    ("paintnsip", "Paint & Sip"),
    ("farmersmarket", "Farmer’s Market"),
    ("vineyard", "Vineyard"),
    ("bakery", "Bakery"),
    ("catering", "Catering/ Chef"),
    ("coffee", "Coffee/Tea/Beverages"),
    ("fooddelivery", "Food Delivery Service"),
    ("icecream", "Ice Cream Parlor"),
    ("alcohol", "Alcohol"),
    ("specialty", "Specialty"),
    ("addiction", "Addiction Treatment"),
    ("chiropractor", "Chiropractor"),
    ("fitness", "Fitness/ Yoga"),
    ("spa", "Spa/ Massage Therapy"),
    ("mentalhealth", "Mental Health Support"),
    ("nutrition", "Nutrition"),
    ("furniture", "Furniture"),
    ("landscaping", "Landscaping/Gardening"),
    ("interiordesign", "Interior Design/ Home Staging"),
    ("pestcontrol", "Pest Control"),
    ("homegoods", "Home Goods/Décor"),
    ("travelagent", "Travel Agent"),
    ("hospitality", "Hospitality/Hotels/Inns"),
    ("tours", "Tours"),
    ("accessories", "Accessories/ Handbags"),
    ("finejewelry", "Fine Jewelry"),
    ("financialservices", "Financial Services"),
    ("notary", "Notary"),
    ("bail", "Bail Bonds Service"),
    ("legal", "Legal Services (General)"),
    ("realestatelaw", "Real Estate Law"),
    ("estateplanning", "Estate Planning/Wills"),
    ("corporatelaw", "Corporate Law"),
    ("insurance", "Insurance"),
    ("adultnovelties", "Adult Novelties"),
    ("cbd", "CBD Products"),
    ("smoking", "Smoking & Paraphernalia"),
    ("tarot", "Tarot"),
    ("piercing", "Piercing/ Tattoos"),
    ("advertising", "Advertising"),
    ("branding", "Branding/ Graphic Design"),
    ("marketing", "Marketing/ Digital Marketing"),
    ("webservices", "Web Services/ Social Media"),
    ("dental", "Dental/ Orthodontics"),
    ("medbilling", "Medical Billing"),
    ("physicaltherapy", "Physical Therapy"),
    ("speechpath", "Speech Pathologist"),
    ("diagnostic", "Diagnostic Testing/Labs"),
    ("vision", "Vision"),
    ("healthproducts", "Healthcare Products"),
    ("primarycare", "Primary Care"),
    ("obgyn", "OB/GYNs"),
    ("pediatrics", "Pediatrics"),
    ("dermatology", "Dermatology"),
    ("psychiatry", "Psychiatry/Mental Health"),
    ("antiques", "Antiques & Collectibles"),
    ("guns", "Guns & Shooting Ranges"),
    ("gifts", "Gifts & Stationery"),
    ("mortuary", "Mortuary/ Funeral Services"),
    ("marketplace", "Marketplace"),
    ("translation", "Translation Services"),
    ("officesupplies", "Office Supplies"),
    ("courier", "Courier"),
    ("printing", "Printing"),
    ("shipping", "Shipping"),
    ("dogtraining", "Dog Training"),
    ("petsitting", "Pet Sitting/ Walking"),
    ("vet", "Veterinarian"),
    ("petgrooming", "Pet Grooming"),
    ("videography", "Videography"),
    ("photography", "Photography"),
    ("consulting", "Consulting"),
    ("humanresources", "Human Resources"),
    ("it", "IT"),
    ("recruiting", "Recruiting/ Staffing"),
    ("privateinvestigator", "Private Investigator"),
    ("writingservices", "Writing Services"),
    ("speakers", "Speakers"),
    ("adminsupport", "Administrative Support"),
    ("developers", "Developers"),
    ("homeinspection", "Home Inspection"),
    ("mortgageconsulting", "Mortgage Consulting"),
    ("propertymanagement", "Property Management"),
    ("realestateagents", "Real Estate Agents/ Brokers"),
    ("titleservices", "Title Services"),
    ("arcade", "Arcade/Laser Tag"),
    ("sports", "Sports"),
    ("martialarts", "Martial Arts"),
    ("sportsequipment", "Sports Equipment"),
    ("pooltables", "Pool Tables"),
    ("gaming", "Gaming"),
    ("bar", "Bar/Night Club"),
    ("bbq", "BBQ/ Soul Food Restaurant"),
    ("cafe", "Café"),
    ("caribbean", "Caribbean Restaurant"),
    ("creole", "Creole/Cajun Restaurant"),
    ("ethiopian", "Ethiopian/Eritrean Restaurant"),
    ("venues", "Venues/Event Spaces"),
    ("westafrican", "West African Restaurant"),
    ("foodtrucks", "Food Trucks/Carts"),
    ("commuter", "Commuter/Shuttle Services"),
    ("mortuarytransport", "Mortuary Transport"),
    ("moving", "Moving Services"),
    ("parking", "Parking"),
    ("taxi", "Taxi"),
    ("limo", "Limo/ Party Bus"),
    ("trucking", "Trucking"),
    ("valet", "Valet"),
    ("artgallery", "Art Gallery/ Museum"),
    ("dance", "Dance Studios/Lessons"),
    ("artists", "Artists"),
    ("theater", "Theater/Acting Lessons"),
    ("music", "Music Lessons/Instruments"),
)
YEARS_IN_BUSINESS_CHOICES = (
    ('<2', '<2 Years'),
    ('3-5', '3-5 Years'),
    ('5-10', '5-10 Years'),
    ('10-15', '10-15 Years'),
    ('>15', '>15 Years'),
)

EMPLOYEES_CHOICES = (
    ('0-4', '0-4 People'),
    ('5-10', '5-10 People'),
    ('11-20', '11-20 People'),
    ('21-30', '21-30 People'),
    ('>30', '>30 People'),
)
REVENUE_CHOICES = (
    ('<$50,000', '<$50,000'),
    ('$51,000-$100,000', '$51,000-$100,000'),
    ('$101,000-$250,000', '$101,000-$250,000'),
    ('$251,000-$500,000', '$251,000-$500,000'),
    ('>$500,000', '>$500,000'),
)
CONCERNS_CHOICES = (
    ('revenue', 'Revenue/Sales'),
    ('financing', 'Business Loans/Acquire Financing'),
    ('staffing', 'Staffing/Employees'),
    ('exiting', 'Exiting'),
    ('marketing', 'Marketing/Advertising'),
    ('ecommerce', 'E-Commerce'),
    ('estate', 'Estate Planning'),
    ('other', 'other')
)
STRUCTURE_CHOICES = (
    ('unincorporated', 'Sole Proprietorship (Unincorporated)'),
    ('incorporated', 'Incorporated Entity'),
    ('partnership', 'Official Partnership'),
    ('llc', 'LLC'),
    ('none', 'None of the above')
)

class BusinessForm(forms.Form):
    nominator_name = forms.CharField(label='Your Name', widget=forms.TextInput(attrs={'class':'textfield',}), label_suffix='', required=True)
    nominator_email = forms.EmailField(label='Your Email Address', widget=forms.EmailInput(attrs={'class':'textfield'}), label_suffix='', required=True)
    business_name = forms.CharField(label='Business Name', widget=forms.TextInput(attrs={'class':'textfield'}), label_suffix='', required=True)
    owner_name = forms.CharField(label='Name of Business Owner(s)', widget=TextInput(attrs={'class':'textfield'}), label_suffix='', required=True)
    years_in_business = forms.CharField(label="What is the # of years in business?", widget=forms.Select(choices=YEARS_IN_BUSINESS_CHOICES), label_suffix='', required=True)
    employees = forms.CharField(label="How many employees do you have?", widget=forms.Select(choices=EMPLOYEES_CHOICES), label_suffix='', required=True)
    revenue = forms.CharField(label="What is your estimated 2021 revenue", widget=forms.Select(choices=REVENUE_CHOICES), label_suffix='', required=True)
    concerns = forms.CharField(label="Which of these most concern you as a business owner? Rank your Top 3 in priority order from 1-3", widget=forms.Select(choices=CONCERNS_CHOICES), label_suffix='')
    structure = forms.CharField(label="Is your business already formed filed as:", widget=forms.Select(choices=STRUCTURE_CHOICES), label_suffix='')
    website = forms.CharField(label='Business Website (optional)', widget=forms.TextInput(attrs={'class':'textfield'}), label_suffix='', required=False)
    instagram = forms.CharField(label='Instagram', widget=forms.TextInput(attrs={'class':'textfield', 'placeholder':'@Instagram'}), label_suffix='', required=False)
    facebook = forms.CharField(label='Facebook', widget=forms.TextInput(attrs={'class':'textfield', 'placeholder':'@Facebook'}), label_suffix='', required=False)
    twitter= forms.CharField(label='Twitter', widget=forms.TextInput(attrs={'class':'textfield', 'placeholder':'@Twitter'}), label_suffix='', required=False)
    phone = forms.CharField(label='Business Phone', widget=forms.TextInput(attrs={'class':'textfield phone_us'}), label_suffix='', required=True)
    category = forms.CharField(label='Category', widget=forms.Select(choices=CATEGORY_CHOICES), label_suffix='', required=True)
    subcategory = forms.CharField(label='Sub-Category', widget=forms.Select(choices=SUBCATEGORY_CHOICES), label_suffix='', required=False)
    online_only = forms.ChoiceField(label='Does this business operate online only?', widget=forms.RadioSelect(), label_suffix='', choices=TRUEFALSE_CHOICES, required=False)
    city = forms.CharField(label='Business City', widget=forms.TextInput(attrs={'class':'textfield'}), label_suffix='', required=True)
    state = forms.CharField(label='Business State', widget=forms.Select(choices=STATE_CHOICES), label_suffix='', required=True)
    individual_state = forms.CharField(label='State', widget=forms.Select(choices=STATE_CHOICES), label_suffix='', required=True)
    owned = forms.ChoiceField(label='Do you own this business?', widget=forms.RadioSelect(choices=TRUEFALSE_CHOICES,), label_suffix='', choices=TRUEFALSE_CHOICES, required=False)
    recommended = forms.ChoiceField(label='Have you used the product or service(s) offered by this business and recommend it to others?', widget=forms.RadioSelect(choices=TRUEFALSE_CHOICES),choices=TRUEFALSE_CHOICES, required=False)
    
    def save(self):
            vbp = super(BusinessForm, self).save()
            return vbp
    
    def get_categories(self):
        categories = CATEGORY_CHOICES
        return categories