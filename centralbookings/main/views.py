from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from Profile.models import Activity_Schedule

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
        formset = CreateFormSet(request.POST, queryset=Job.objects.none())

        if form.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user.profile
            commission.save()

            if formset.is_valid():
                for job_form in formset:
                    if job_form.cleaned_data:
                        job = job_form.save(commit=False)
                        job.commission = commission
                        job.save()

            return redirect('commissions:commission_detail', pk=commission.pk)
    else:
        form = CommissionForm()
        formset = JobFormSet(queryset=Job.objects.none())

    return render(request, 'create_form.html', {'create_form': form,'create_formset': formset})
