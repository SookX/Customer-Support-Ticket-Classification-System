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
    
@api_view(['GET', 'PATCH', 'DELETE', 'POST'])
def system_details(request, id):

    """
    Handles retrieval, partial updates, and deletion of a specific System record.

    Methods:
    - GET: 
        - Retrieves the details of a specific system based on its ID.
        - Returns a JSON object containing the system's name, the holder's username, the system's description, and a list of usernames of associated admins.

    - PATCH: 
        - Allows for partial updates of the system's fields.
        - Updates the system's name and description if provided in the request.
        - Adds new admins to the system without removing existing ones. If any admin IDs are provided, the corresponding users are retrieved and added as admins.
        - Returns a success message upon successful update.

    - DELETE: 
        - Deletes the system identified by the provided ID.
        - Returns a success message confirming the deletion.

    - POST: 
        - This method is not allowed for this endpoint and returns a 405 Method Not Allowed error.

    Returns:
    - GET:
        - 200 OK: A JSON response with the system's details (name, holder username, description, and admins).
        - 404 Not Found: If the system with the specified ID does not exist.

    - PATCH:
        - 200 OK: A JSON response with a success message indicating that the system was updated.
        - 404 Not Found: If any specified admin ID does not exist.

    - DELETE:
        - 204 No Content: A success message indicating that the system was deleted.
        - 404 Not Found: If the system with the specified ID does not exist.

    - POST:
        - 405 Method Not Allowed: Indicates that POST requests are not supported at this endpoint.
    """
    
    system = get_object_or_404(System, id=id)

    if request.method == "GET":
        data = {
            'name': system.name,
            'holder': system.holder.username,
            'description': system.description,
            'admins': [admin.username for admin in system.admins.all()]
        }
        return Response(data)
    
    if request.method == "PATCH":
        name = request.data.get('name')
        description = request.data.get('description')
        admins_ids = request.data.get('admins', [])

        if name:
            system.name = name
        if description:
            system.description = description

        if admins_ids:
            for admin_id in admins_ids:
                admin = get_object_or_404(CustomUser, id=admin_id)
                system.admins.add(admin)

        system.save()

        return Response({"message": "System updated successfully"}, status=status.HTTP_200_OK)
    
    if request.method == "DELETE":
        system.delete()
        return Response({"message": "System deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == "POST":
        return Response({"error": "POST method not allowed for this endpoint"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)