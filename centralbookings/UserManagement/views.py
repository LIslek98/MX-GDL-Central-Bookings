from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.urls import reverse_lazy

from .models import Organizer, Participant
from .forms import OrganizerForm, ParticipantForm




# implementations not full, commenting out for now to avoid errors

# def register(request):
#     form = RegisterForm()
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('choose_account_type')   
#     return render(request, 'registration/register.html', {'regform': form})

# def participantRegister(request):
#     if request.method == 'POST':
#         form = ParticipantForm(request.POST)
#         if form.is_valid():
#             participant = form.save(commit=False)
#             participant.user = request.user
#             participant.save()
#             return redirect('home_page')
#         else:
#             form = ParticipantForm()
#     return render(request, 'participantForm.html', {'participant_form': form, 'particpant': participant})
13

class BasicLoginPageView(DetailView):
    model = User
    template_name = "login_page.html"

class ParticipantCreateView(CreateView):
    model = User
    template_name = "participant_register.html"

    def form_valid(self, form):
        new_user = form.save()
        display_name = form.cleaned_data['display_name']
        Participant.objects.create(
            user=new_user, name=display_name, email=new_user.email)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("login")

class OrganizerCreateView(CreateView):
    model = User
    template_name = "organizer_register.html"

    def form_valid(self, form):
        new_user = form.save()
        display_name = form.cleaned_data['display_name']
        Profile.objects.create(
            user=new_user, name=display_name, email=new_user.email)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("login")




