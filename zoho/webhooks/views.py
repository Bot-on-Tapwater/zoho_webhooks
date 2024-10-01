from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import ZohoFormData

@csrf_exempt
def zoho_webhook(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON payload
            data = json.loads(request.body)

            # Extract fields from the incoming data
            field1 = data.get('field1', None)
            field2 = data.get('field2', None)
            field3 = data.get('field3', None)
            field4 = data.get('field4', None)
            field5 = data.get('field5', None)
            field6 = data.get('field6', None)
            field7 = data.get('field7', None)
            field8 = data.get('field8', None)
            field9 = data.get('field9', None)
            field10 = data.get('field10', None)
            field11 = data.get('field11', None)
            field12 = data.get('field12', None)
            field13 = data.get('field13', None)
            field14 = data.get('field14', None)
            field15 = data.get('field15', None)
            field16 = data.get('field16', None)
            field17 = data.get('field17', None)
            field18 = data.get('field18', None)
            field19 = data.get('field19', None)

            # Save the form data to the database
            ZohoFormData.objects.create(
                field1=field1,
                field2=field2,
                field3=field3,
                field4=field4,
                field5=field5,
                field6=field6,
                field7=field7,
                field8=field8,
                field9=field9,
                field10=field10,
                field11=field11,
                field12=field12,
                field13=field13,
                field14=field14,
                field15=field15,
                field16=field16,
                field17=field17,
                field18=field18,
                field19=field19,
            )

            logging.info("Form data saved successfully.")
            return JsonResponse({"status": "success", "message": "Data received and saved successfully"})

        except json.JSONDecodeError:
            logging.error("Failed to decode JSON data.")
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return JsonResponse({"status": "error", "message": f"An error occurred: {e}"}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

def list_zoho_forms(request):
    """API view to return all stored Zoho form data as JSON."""
    forms = ZohoFormData.objects.all().values()  # Retrieve all form data as dictionaries
    return JsonResponse(list(forms), safe=False)
