from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def dashboard(request):

    context = {
        
    }
    return render(request, 'patient/patient-dashboard.html', context)