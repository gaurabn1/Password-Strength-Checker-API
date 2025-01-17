from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSignupSerializer, PasswordStrengthSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .utility import evaluate_password_strength
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Password Strength Checker
class PasswordStrengthCheckerView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=PasswordStrengthSerializer, manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)])
    def post(self, request):
        serializer = PasswordStrengthSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            result = evaluate_password_strength(password)
            return Response(result, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Signup API
class UserSignupView(APIView):

    @swagger_auto_schema(request_body=UserSignupSerializer)
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#GET API Token
class GetAPITokenView(APIView):
    def post(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token' : token.key,
                'message' : 'Your API Token'
            }, status=status.HTTP_200_OK)

