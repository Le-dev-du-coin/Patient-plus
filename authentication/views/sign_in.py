from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages


def signin(request):
    if request.user.is_authenticated:
        if user.is_doctor:
            return redirect('doctor-home')
        else:
            return redirect('patient-home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                print('Connecter')
                if user.is_patient:
                    return redirect('patient-home')
                else:
                    return redirect('doctor-home')
            else:
                print("erreur d'informations")
                messages.error(request, "Une erreur s'est produite verifier vos informations")
                return render(request, 'authentication/login.html')
        else:
                messages.error(request, "Une erreur s'est produite verifier vos informations")
                return render(request, 'authentication/login.html')
