from django.db import models

class Appointment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    message = models.TextField()

    class Meta:
        db_table = 'appointment_table'

    def __str__(self):
        return self.full_name
