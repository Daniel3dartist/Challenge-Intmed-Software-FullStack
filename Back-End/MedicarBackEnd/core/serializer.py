from .models import Doctor, Schedule
from rest_framework import serializers

#class DoctorSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Doctor
#        fields = ["first_name", "and_name", "crm", "email"]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["appointment_doctor", "appointment_day", "appointment_time", "appointment_registration_date"]