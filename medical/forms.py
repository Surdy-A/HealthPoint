from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Patient, Practitioner
from django.forms import ModelForm


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class MedPractitionerForm(ModelForm):
    class Meta:
        model = Practitioner
        fields = '__all__'
