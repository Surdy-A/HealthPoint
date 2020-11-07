from django.urls import path
from .views import patient_register, HomePageView

urlpatterns = [
    path('patient/', patient_register, name="patient"),
    path('practitioner/', patient_register, name="practitioner"),
    path('', HomePageView.as_view(), name='home')
]
