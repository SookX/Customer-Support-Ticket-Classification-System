from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import System, CustomUser

@api_view(['POST', 'GET'])
def system_view(request):
    
    """
    Handles the creation and retrieval of System records.

    Methods:
    - POST: 
        - Receives a request to create a new system. The request must include a name, holder ID, and description.
        - Validates that `name`, `holder`, and `description` fields are provided.
        - Retrieves the `CustomUser` associated with the holder ID. If not found, returns a 404 response.
        - Attempts to create a new `System` with the provided name, holder, and description.
        - Optionally, if a list of admin IDs is provided, it adds the corresponding users as admins for the system.
        - Returns a response indicating successful system creation along with the system's ID.

    - GET:
        - Retrieves all existing systems from the database.
        - Returns a list of system objects, including each system's ID, name, holder's username, description, and admin usernames.
        - Responds with a 200 status code upon success.

    Returns:
    - POST: 
        - 201 Created: A JSON response with a success message and the created system's ID.
        - 400 Bad Request: If any required fields (`name`, `holder`, `description`) are missing or if an error occurs during system creation.
        - 404 Not Found: If the holder or any of the provided admins do not exist.

    - GET: 
        - 200 OK: A list of systems as a JSON response, including system details (ID, name, holder username, description, and admin usernames).
    """


    if request.method == "POST":
        name = request.data.get('name')
        holder_id  = request.data.get('holder')
        description = request.data.get('description')
        admins_ids = request.data.get('admins', [])

        if not all([name, holder_id, description]):
            return Response({"error": "Missing required fields"}, status=status.HTTP_400_BAD_REQUEST)
        
        holder = get_object_or_404(CustomUser, id=holder_id)

        try:
            system = System.objects.create(name=name, holder=holder, description=description)
            
            if admins_ids:
                for admin_id in admins_ids:
                    admin = get_object_or_404(CustomUser, id=admin_id)
                    system.admins.add(admin)

            return Response({"message": "System created successfully", "system_id": system.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        data = System.objects.values('id', 'name', 'holder__username', 'description', 'admins__username')
        return Response(list(data), status=status.HTTP_200_OK)