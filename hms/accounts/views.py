from rest_framework import generics
from .models import User
from .serializers import UserSignupSerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignupSerializer, LoginSerializer
from utils.email_service import send_email

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    def perform_create(self, serializer):
        user = serializer.save()

        send_email(
            "SIGNUP_WELCOME",
            user.email
        )
    

class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return Response({
                "message": "Login Successful",
                "role": user.role
            })

        return Response(
            {"error": "Invalid Credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )