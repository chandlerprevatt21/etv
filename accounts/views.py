from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.views.generic import CreateView, FormView, DetailView, View, UpdateView, ListView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.utils.http import is_safe_url
from django.utils.safestring import mark_safe
from .forms import LoginForm, RegisterForm, GuestForm, UserTeamForm
from bfchallenge.models import nomination
from accounts.models import Team

from etv.mixins import NextUrlMixin, RequestFormAttachMixin
from .models import GuestEmail
from .signals import user_logged_in

from django.shortcuts import render, redirect
import sweetify

User = get_user_model()

def AccountHomeView(request):
    nomination_qs = nomination.objects.filter(user=request.user).count()
    context = {
        'nomination_qs': nomination_qs
    }
    return render(request, 'accounts/home.html', context)

class GuestRegisterView(NextUrlMixin, RequestFormAttachMixin, CreateView):
    form_class = GuestForm
    default_next = '/register/'

    def get_success_url(self):
        return self.get_next_url()

    def form_invalid(self, form):
        return redirect(self.default_next)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teams = Team.objects.all()
        context["team_list"] = teams
        return context

def JoinTeam(request):
    context = {
        'title': 'ETV | Join Team'
    }
    if request.method == 'POST':
        form = UserTeamForm(request.POST)
        form_team = form.data['team']
        obj, created = Team.objects.get_or_create(
            team_name=form_team
        )
        obj.save()
        user = request.user
        user.team = obj
        user.save()
        sweetify.success(request, title='Thank you!', icon='success', text="You've successfully joined a team!", button='OK', timer=4000)
        return redirect('/account/my-account/')
    else:
        form = UserTeamForm(instance=request.user)
        context={
            'form': UserTeamForm(),
            'teams': Team.objects.all()
        }
    return render(request, 'accounts/join-team.html', context)

class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    success_url = '/'
    template_name = 'accounts/sociallogin.html'
    default_next = '/'
    register_form = RegisterForm

    def form_valid(self, form):
            next_path = self.get_next_url()
            return redirect(next_path)
