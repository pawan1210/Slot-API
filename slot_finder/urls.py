from django.urls import path
from .views import SlotFinderView

urlpatterns = [
    path("find_slot", SlotFinderView.as_view()),
]
