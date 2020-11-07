from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .forms import PatientForm, MedPractitionerForm


class HomePageView(TemplateView):
    template_name = 'patient/home.html'


def patient_register(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request, ('You Have Save a Patience record...'))
            return redirect('home')
    else:
        form = PatientForm()

    context = {'form': form}
    return render(request, 'patient/patient_signup.html', context)


def practitioner(request):
    if request.method == 'POST':
        form = MedPractitionerForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            messages.success(request,
                             ('You Have Save a Practitioner record...'))
            return redirect('home')
    else:
        form = MedPractitionerForm()

    context = {'form': form}
    return render(request, 'patient/med_practitioner.html', context)
