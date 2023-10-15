from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from .models import Doctor, Schedule

class DoctorAdminForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
    
    def clean_crm(self):
        _crm = self.cleaned_data["crm"]
        if Doctor.objects.filter(crm=_crm).exists():
            doctor = Doctor.objects.get(crm=_crm)
            if str(doctor.first_name + ' ' + doctor.end_name) != str(self.cleaned_data['first_name'] + ' ' + self.cleaned_data['end_name']):
                raise ValidationError("CRM is already being used.")
        return self.cleaned_data["crm"]

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("first_name", 'crm', "email")
    fields = ('first_name', 'end_name', 'crm', 'email')
    form = DoctorAdminForm

admin.site.register(Schedule)