from django.shortcuts import render
from .models import Schedule
from .serializer import ScheduleSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class ConsultasViewSet(APIView):
    def get(self, request, format=None):
        schedule = Schedule.objects.all()
        serializer = ScheduleSerializer(schedule, many=True)
        return Response(serializer.data)