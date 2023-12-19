from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Home view
def home(request):
    context = {}
    return render(request, "core/index.html", context)

@login_required(login_url='login')
def patientHome(request):
    return render(request, 'core/patient-home.html')

@login_required(login_url='login')
def doctorHome(request):
    return render(request, 'core/doctor-home')