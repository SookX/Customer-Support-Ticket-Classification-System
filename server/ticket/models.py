from django.db import models
from system.models import System

class Ticket(models.Model):
    
    """
    Represents a ticket related to a system issue or request.

    Attributes:
        subject (str): The subject or title of the ticket.
        class_prediction (str): A classification or category prediction for the ticket.
        status (str): The current status of the ticket.
        system (ForeignKey): The system associated with the ticket.
    """
    
    subject = models.CharField(max_length=512)
    class_prediction = models.CharField(max_length=256)
    status = models.BooleanField(default=1)
    system = models.ForeignKey(System, on_delete=models.CASCADE, related_name="ticket_system", null=False)