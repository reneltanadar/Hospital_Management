from django.urls import path
from .views import AvailabilityCreateView
from .views import (
    AvailabilityCreateView,
    AvailabilityListView
)

urlpatterns = [
    path("availability/", AvailabilityCreateView.as_view(), name="availability"),
    path(
        "available-slots/",
        AvailabilityListView.as_view(),
        name="available-slots"
    ),
]