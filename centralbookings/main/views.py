from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Activity_Schedule
from .forms import ActivityScheduleForm

def activity_list(request):
    scheds = Activity_Schedule.objects.all()
    context = {
        'activities': scheds
    }
    return render(request, 'activitylist.html', context)

@login_required
def activity_create(request):
    form = ActivityScheduleForm()
    
    if request.method == 'POST':
        form = ActivityScheduleForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('activitylist')
    else:
        form = ActivityScheduleForm()

    return render(request, 'create_form.html', {'create_form': form})
