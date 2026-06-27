from django.db import transaction

from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from doctors.models import Availability
from .models import Booking
from .serializers import BookingSerializer
from calendar_service.google_calendar import create_calendar_event
from utils.email_service import send_email


class BookAppointmentView(generics.CreateAPIView):

    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def perform_create(self, serializer):

        if self.request.user.role != "patient":
            raise ValidationError(
                "Only patients can book appointments."
            )

        availability_id = self.request.data.get("availability")

        slot = Availability.objects.select_for_update().get(
            id=availability_id
        )

        if slot.is_booked:
            raise ValidationError(
                "This slot has already been booked."
            )

        slot.is_booked = True
        slot.save()

        booking = serializer.save(
        patient=self.request.user,
        availability=slot
        )

        send_email(
    "BOOKING_CONFIRMATION",
    self.request.user.email
)

    # # Google Calendar Integration
    #     create_calendar_event(
    #         access_token="YOUR_ACCESS_TOKEN",
    #         doctor_email=slot.doctor.email,
    #         patient_email=self.request.user.email,
    #         start_datetime=slot.start_time,
    #         end_datetime=slot.end_time,
    #         doctor_name=slot.doctor.username,
    #         patient_name=self.request.user.username,
    #     )