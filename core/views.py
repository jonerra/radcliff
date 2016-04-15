from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import *
from .forms import *

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

class PlayerRoster(ListView):
    model = Player
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
    
class FieldList(ListView):
    model = Field
    template_name = "fields/field_list.html"
    # success_url = reverse_lazy('success')
    
class FieldDetail(DetailView):
    model = Field
    template_name = "fields/field_detail.html"
    
# class FieldUpdateView(UpdateView):
    # model = Field
    # form = FieldUpdateForm
    # success_url = reverse_lazy('field')
    # template_name = "fields/field_form.html"
    
class FieldReservationCreateView(CreateView):
    model = Reservation
    #form = ReservationUpdateView
    success_url = reverse_lazy('field_list')
    template_name = "fields/reservation_form.html"
    fields = ['Date', 'Time', 'FieldID', 'VolunteerID']
    
class FieldReservationUpdateView(UpdateView):
    model = Reservation
    #form = ReservationUpdateView
    success_url = reverse_lazy('field_list')
    template_name = "fields/reservation_form.html"
    fields = ['Date', 'Time', 'FieldID', 'VolunteerID']