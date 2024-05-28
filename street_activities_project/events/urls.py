from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.events_list),
    path("events/<int:pk>/", views.events_detail),
]
