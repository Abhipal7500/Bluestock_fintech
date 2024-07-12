from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer, UserLoginSerializer
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import UnverifiedUser
from rest_framework_simplejwt.tokens import RefreshToken
from account.renderer import UserRenderer
User = get_user_model()

#generate token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            unverified_user = serializer.save()
            return Response({'msg': 'Registration Successful. Please verify your email.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        email = request.data.get('email')
        verification_code = request.data.get('verification_code')

        unverified_user = get_object_or_404(UnverifiedUser, email=email, verification_code=verification_code)
        
        # Create the user
        user = User.objects.create_user(
            email=unverified_user.email,
            username=unverified_user.username,
            first_name=unverified_user.first_name,
            last_name=unverified_user.last_name,
            password=unverified_user.password
        )
        user.email_verified = True
        user.save()
        token= get_tokens_for_user(user)
        # Delete the unverified user record
        unverified_user.delete()

        return Response({'token':token, 'msg': 'Email verified successfully'}, status=status.HTTP_200_OK)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                if user.email_verified:
                    token= get_tokens_for_user(user)
                    return Response({'token':token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
                else:
                    return Response({'errors': {'email': 'Email not verified'}}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
