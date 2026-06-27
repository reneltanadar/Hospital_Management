from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Availability
from .serializers import AvailabilitySerializer
from django.utils import timezone

class AvailabilityCreateView(generics.CreateAPIView):

    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        if self.request.user.role != "doctor":
            raise PermissionDenied(
                "Only doctors can create availability."
            )

        serializer.save(doctor=self.request.user)

class AvailabilityListView(generics.ListAPIView):

    serializer_class = AvailabilitySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        return Availability.objects.filter(
            is_booked=False,
            date__gte=timezone.now().date()
        ).order_by("date", "start_time")