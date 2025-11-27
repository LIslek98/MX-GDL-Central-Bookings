from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

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
