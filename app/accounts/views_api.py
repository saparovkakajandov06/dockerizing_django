from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        if "email" not in request.data:
            return Response({"message": "Email is required!"}, status=status.HTTP_400_BAD_REQUEST)
        if "password" not in request.data:
            return Response({"message": "Password is required!"}, status=status.HTTP_400_BAD_REQUEST)
        if "password2" not in request.data:
            return Response({"message": "Password confirmation is required!"}, status=status.HTTP_400_BAD_REQUEST)
        if request.data["password"] != request.data["password2"]:
            return Response({"message": "Passwords must match!"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "User created successfully!"})
