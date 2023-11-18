from django.urls import path

from . import views

urlpatterns = [
    path("view/", views.events, name="events"),
    path("apply/", views.apply, name="apply"),
]