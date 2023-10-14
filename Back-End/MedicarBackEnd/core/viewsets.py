from rest_framework import viewsets
from .models import Schedule
from .serializer import ScheduleSerializer


class ConsultasViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer