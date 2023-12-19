from django.shortcuts import render, redirect

def register(request):

    context = {
        
    }
    return render(request, 'authentication/doctor-register.html', context)