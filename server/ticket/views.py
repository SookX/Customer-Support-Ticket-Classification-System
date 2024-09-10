from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Ticket
import json
from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET'])
def ticket_view(request):
   
    """
    Handles the creation of new tickets and retrieval of all tickets.

    Methods:
    - POST: Creates a new ticket with the given subject, status, and a placeholder for class prediction.
    - GET: Returns a list of all tickets.

    Returns:
    - POST: A response with the created ticket data or an error message if validation fails.
    - GET: A response with a list of all existing tickets.
    """
    
    if request.method == "POST":
        subject = request.data.get('subject')
        status_var = request.data.get('status')
        
        if not subject:
            return Response({"error": "Subject is required."}, status=status.HTTP_400_BAD_REQUEST)

        ticket = Ticket.objects.create(subject=subject, class_prediction="Pending Prediction", status=status_var)
        
        ticket_data = {
            "id": ticket.id,
            "subject": ticket.subject,
            "class_prediction": ticket.class_prediction,
            "status": ticket.status,
        }
        return Response(ticket_data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        data = Ticket.objects.values('id', 'subject', 'class_prediction', 'status')
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