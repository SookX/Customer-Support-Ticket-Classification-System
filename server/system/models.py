from django.db import models
from accounts.models import CustomUser

class System(models.Model):

    """
    Represents a system within the application.

    Attributes:
        name (str): The name of the system.
        holder (ForeignKey): The primary user responsible for the system.
        description (str): A brief description of the system.
        admins (ManyToManyField): A list of users who have admin access to the system.
    """

    name = models.CharField(max_length=256)
    holder = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='holder', null=False)
    description = models.CharField(max_length=512)
    admins = models.ManyToManyField(CustomUser, related_name='admin_systems', blank=True)