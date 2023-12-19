from django.urls import path
from core.views import home


urlpatterns = [
    path("", home.home, name="home"),
    path('acceuil-patient', home.patientHome, name='patient-home'),
    path('acceuil-doctor', home.doctorHome, name='doctor-home'),
]
