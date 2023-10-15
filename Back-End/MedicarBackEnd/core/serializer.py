from .models import Doctor, Schedule
from rest_framework import serializers

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["appointment_doctor", "appointment_day", "appointment_times", "appointment_registration_date"]