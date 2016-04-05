from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
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

class VolunteerRegistration(CreateView):
    model = Volunteer
    template_name = "registration/volunteer_registration.html"
    fields = ["FirstName", "LastName", "DateOfBirth", "Street", "City", "State", "Zipcode", "PhoneNumber", "Email", "Returning", "Children"]
    success_url = reverse_lazy('success')

class Success(TemplateView):
    template_name = "success.html"

class PlayerRoster(TemplateView):
    template_name = "roster.html"

class LeagueUpdate(CreateView):
    model = Update
    template_name = "update/league_update.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('success')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LeagueUpdate, self).form_valid(form)
        
class UpdateList(ListView):
    model = Update
    template_name = "update/update_list.html"
    
class ReserveField(CreateView):
    model = Reservation
    template_name = "fields.html"
    fields = ['FieldName', 'Date']
    success_url = reverse_lazy('success')