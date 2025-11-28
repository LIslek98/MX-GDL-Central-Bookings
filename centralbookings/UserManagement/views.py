from django.contrib.auth.models import User
from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .models import Organizer, Participant
from .forms import UserForm, ParticipantForm, OrganizerForm, ContactPersonForm

class HomepageView(ListView):
    model = User
    template_name = 'homepage.html'

class ParticipantRegisterView(View):
    template_name = "participant_register.html"
    success_url = reverse_lazy('UserManagement:register')

    def get(self, request):
        return render(request, self.template_name, {
            "user_form": UserForm(),
            "participant_form": ParticipantForm()
        })

    def post(self, request):
        user_form = UserForm(request.POST)
        participant_form = ParticipantForm(request.POST)

        if user_form.is_valid() and participant_form.is_valid():
            user = user_form.save()

            participant = participant_form.save(commit=False)
            participant.user = user
            participant.save()

            return redirect(self.success_url)

        return render(request, self.template_name, {
            "user_form": user_form,
            "participant_form": participant_form
        })

class OrganizerRegisterView(View):
    template_name = "organizer_register.html"
    success_url = reverse_lazy('UserManagement:register')

    def get(self, request):
        return render(request, self.template_name, {
            "user_form": UserForm(),
            "contact_form": ContactPersonForm(),
            "organizer_form": OrganizerForm()
        })

    def post(self, request):
        user_form = UserForm(request.POST)
        contact_form = ContactPersonForm(request.POST)
        organizer_form = OrganizerForm(request.POST)

        if user_form.is_valid() and contact_form.is_valid() and organizer_form.is_valid():
            user = user_form.save()

            contact_person = contact_form.save()

            organizer = organizer_form.save(commit=False)
            organizer.user = user
            organizer.contact_person = contact_person
            organizer.save()

            return redirect(self.success_url)

        return render(request, self.template_name, {
            "user_form": user_form,
            "contact_form": contact_form,
            "organizer_form": organizer_form
        })


