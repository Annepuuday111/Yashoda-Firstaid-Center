from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Appointment

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def login(request):
    return render(request, 'login.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def booking(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Appointment Added Successfully")
        else:
            print(form.errors)
    else:
        form = AppointmentForm()
    return render(request, 'booking.html', {'form': form})


def admindashboard(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'admindashboard.html', context)

