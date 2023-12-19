from django.urls import path
from patient.views import patient_dashboard, patient_home

urlpatterns = [
    path('home/', patient_home.home, name="patient-home"),
    path('dashboard/',patient_dashboard.dashboard , name='patient-dashboard'),
]