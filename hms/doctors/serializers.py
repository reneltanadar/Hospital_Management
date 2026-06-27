from rest_framework import serializers
from .models import Availability


class AvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Availability
        fields = "__all__"
        read_only_fields = ["doctor", "is_booked"]

    def validate(self, data):

        if data["start_time"] >= data["end_time"]:
            raise serializers.ValidationError(
                "End time must be after start time."
            )

        return data