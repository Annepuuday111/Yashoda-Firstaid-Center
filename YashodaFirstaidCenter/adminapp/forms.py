
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone_number', 'date', 'message']
        labels = {
            'date': 'Date (MM/DD/YYYY)'
        }
