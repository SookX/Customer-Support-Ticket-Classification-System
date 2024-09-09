# accounts/views.py
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
import json

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
