from django.shortcuts import render, redirect
from authentication.forms import RegisterForm
from authentication.models import Account
from django.contrib import messages

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        # Get the form data
        form = RegisterForm(request.POST)
        if form.is_valid():
           first_name = request.POST['first_name']
           last_name = request.POST['last_name']
           username = request.POST['username']
           email = request.POST['email']
           phone_number = request.POST['phone_number']
           password1 = request.POST['password1']
           password2 = request.POST['password2']

           user = form.save(commit=False)
           user.phone_number = phone_number
           user.is_patient = True

           user.save()
           return redirect('home')

        else:
            form = RegisterForm()
            messages.error(request, 'Une erreur est survenue')
            return render(request, 'authentication/patient-register.html', context = {'form': form})

    context = {"form": form}
    return render(request, "authentication/patient-register.html", context)
