from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class PlayerRegistration(CreateView):
    model = Player
    template_name = "registration/player_registration.html"
    fields = ["GuardianFirstName", "GuardianLastName", "PlayerFirstName", "PlayerLastName", 'DateOfBirth', 'Street', 'City', 'State', 'Zipcode', 'PhoneNumber', 'Level']
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"