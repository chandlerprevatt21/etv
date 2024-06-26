from django.urls import path

from billing.views import braintree_disbursement
from .views import *

urlpatterns = [
    path('', DashboardHome, name="home"),
    path('braintree-dash/', braintree_disbursements, name="braintree-dash"),
    path('create/', new_obj, name="save-new"),
    path('delete/', delete_obj, name="delete"),
    path('save/', save_obj, name="save"),
    path('donor-update/', updateDonors),
    path('<category>/', appHome, name="category"),
    path('<category>/<model>-list/', modelHome, name="model"),
    path('<category>/<model>-list/edit/<pk>', objectChange, name="change"),
    path('<category>/<model>-list/create/', objectNew, name="new"),
    path('<category>/<model>-list/view/<pk>', objectView, name="view"),
]
