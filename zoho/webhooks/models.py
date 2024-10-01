from django.db import models

class ZohoFormData(models.Model):
    field1 = models.CharField(max_length=255, blank=True, null=True)
    field2 = models.CharField(max_length=255, blank=True, null=True)
    field3 = models.CharField(max_length=255, blank=True, null=True)
    field4 = models.CharField(max_length=255, blank=True, null=True)
    field5 = models.CharField(max_length=255, blank=True, null=True)
    field6 = models.CharField(max_length=255, blank=True, null=True)
    field7 = models.CharField(max_length=255, blank=True, null=True)
    field8 = models.CharField(max_length=255, blank=True, null=True)
    field9 = models.CharField(max_length=255, blank=True, null=True)
    field10 = models.CharField(max_length=255, blank=True, null=True)
    field11 = models.CharField(max_length=255, blank=True, null=True)
    field12 = models.CharField(max_length=255, blank=True, null=True)
    field13 = models.CharField(max_length=255, blank=True, null=True)
    field14 = models.CharField(max_length=255, blank=True, null=True)
    field15 = models.CharField(max_length=255, blank=True, null=True)
    field16 = models.CharField(max_length=255, blank=True, null=True)
    field17 = models.CharField(max_length=255, blank=True, null=True)
    field18 = models.CharField(max_length=255, blank=True, null=True)
    field19 = models.CharField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zoho Form Data {self.id}"
