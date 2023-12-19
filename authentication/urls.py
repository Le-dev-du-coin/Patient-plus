from django.urls import path
from authentication.views import patient_register, sign_in, sign_out, doctor_register

urlpatterns = [
    path('inscription/patient', patient_register.register, name='patient-register'),
    path('inscription/docteur', doctor_register.register, name='doctor-register'),
    path('connexion/', sign_in.signin, name='login'),
    path('Deconnexion', sign_out.signout, name='logout')
]
