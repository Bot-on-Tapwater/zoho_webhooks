from django.urls import path
from . import views

urlpatterns = [
    path("webhook/", views.zoho_webhook, name="zoho_webhook"),
    path("forms/", views.list_zoho_forms, name="list_zoho_forms"),
    path("table/data/", views.display_data, name="display_table_data"),
]
