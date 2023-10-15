from django.db import models
from typing import Dict
import json


class Doctor(models.Model):
    first_name = models.CharField(default='' ,max_length=30)
    end_name = models.CharField(default='', max_length=30)
    crm = models.CharField(default='', max_length=13, unique=True)
    email = models.EmailField(default='')

    def __str__(self):
        return f"{self.first_name} {self.end_name}"

class Schedule(models.Model):
    appointment_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_day = models.DateField()
    appointment_times = models.JSONField(default=dict)
    appointment_registration_date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.doctor} | {self.scheduled_day} | {self.scheduled_time}'