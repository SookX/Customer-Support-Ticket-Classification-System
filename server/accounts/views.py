# accounts/views.py
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
import json
from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET'])
def user(request):
    
    """
    Handles user registration and retrieval:
    - POST: Registers a new user with a username and password.
      Responds with 400 Bad Request if username or password is missing,
      or if the username already exists. On success, responds with a 201 Created status.
    - GET: Returns a list of all users.
    """

    if request.method == "POST":
        
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser(username=username, password=make_password(password))
        user.save()

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
    
    if request.method == "GET":
        data = CustomUser.objects.values()
        return Response(list(data))

# login function with JWT tokens auth
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     if not username or not password:
#         return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

#     user = authenticate(username=username, password=password)
#     if user is None:
#         return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

#     refresh = RefreshToken.for_user(user)
#     return Response({
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),    
#     }, status=status.HTTP_200_OK)

@api_view(['GET', 'PATCH', 'DELETE'])
def user_detail(request, id):
    
    """
    Handles user retrieval, updating, and deletion:
    - GET: Retrieves the details of a user by their ID.
      Responds with the user's username. If the user is not found, returns a 404 Not Found status.
    - PATCH: Updates the username of the user with the specified ID.
      Requires a `username` field in the request body. Responds with the updated username on success.
      Responds with 400 Bad Request if the `username` field is missing.
    - DELETE: Deletes the user with the specified ID.
      Responds with a 204 No Content status on successful deletion.
    """
    
    user = get_object_or_404(CustomUser, id=id)

    if request.method == 'GET':
        data = {
            'username': user.username
        }   
        return Response(data)

    if request.method == 'PATCH':
        username = request.data.get('username', None)
        if username:
            user.username = username
            user.save()
            return Response({'username': user.username})
        return Response({'error': 'Username not provided'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
