from django.urls import path
from . import views

urlpatterns = [
    path("notifications/send/", views.send_notifications, name="send-notifications"),
]
