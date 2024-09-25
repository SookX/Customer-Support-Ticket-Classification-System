from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Ticket
import json
from django.shortcuts import get_object_or_404
from system.models import System

@api_view(['POST', 'GET'])
def ticket_view(request):
   
    """
    Handles the creation and retrieval of Ticket records.

    Methods:
    - POST: 
        - Receives a request to create a new ticket. The request must include a subject, status, and system_id.
        - Validates that `system_id` and `subject` are provided.
        - Attempts to retrieve the `System` related to the `system_id`. If the system is not found, returns a 404 response.
        - Creates a new `Ticket` with the provided subject, status, and links it to the specified system.
        - The `class_prediction` field is automatically set to "Pending Prediction" during ticket creation.
        - Returns a response containing the newly created ticket's data (id, subject, class_prediction, status, and system_id) with a 201 status code upon success.

    - GET:
        - Retrieves all existing tickets from the database.
        - Returns a list of ticket objects, including each ticket's id, subject, class_prediction, status, and system_id.
        - Responds with a 200 status code upon success.

    Returns:
    - POST: 
        - 201 Created: A JSON response with the newly created ticket's data.
        - 400 Bad Request: If the `system_id` or `subject` is missing, returns an error message.
        - 404 Not Found: If the system associated with `system_id` does not exist, returns an error message.
    - GET: 
        - 200 OK: A list of tickets as a JSON response.
    """
    
    if request.method == "POST":
        subject = request.data.get('subject')
        status_var = request.data.get('status')
        system_id = request.data.get('system_id')

        if not system_id:
            return Response({"error": "System ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not subject:
            return Response({"error": "Subject is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            system_related = System.objects.get(id=system_id)
        except System.DoesNotExist:
            return Response({"error": "No system with this ID found."}, status=status.HTTP_404_NOT_FOUND)

        ticket = Ticket.objects.create(subject=subject, class_prediction="Pending Prediction", status=status_var, system = system_related)
        
        ticket_data = {
            "id": ticket.id,
            "subject": ticket.subject,
            "class_prediction": ticket.class_prediction,
            "status": ticket.status,
            "system_id": ticket.system.id,
        }
        return Response(ticket_data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        data = Ticket.objects.values('id', 'subject', 'class_prediction', 'status', 'system')
        return Response(list(data), status=status.HTTP_200_OK)
    
@api_view(['GET'])
def ticket_details(request, id):

    """
    Retrieves and returns the details of a specific ticket.

    Args:
    - request (Request): The incoming HTTP request.
    - id (int): The unique identifier of the ticket.

    Returns:
    - Response: A JSON response containing the ticket's subject, class prediction, and status.
    """

    ticket = get_object_or_404(Ticket, id = id)

    data = {
            'subject': ticket.subject,
            'class_prediction': ticket.class_prediction,
            'status': ticket.status
        }   
    return Response(data)