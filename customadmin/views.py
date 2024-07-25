from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers import UserLoginSerializer
from account.renderer import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Generate token
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Admin login view to render the login page
def adminLogin(request):
    return render(request, 'login.html')

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_admin:
                    if user.email_verified:
                        token = get_tokens_for_user(user)
                        response_data = {
                            'token': token,
                            'redirect_url': 'dashboard/'
                        }
                        return Response(response_data, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': {'email': 'Email not verified'}}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'errors': {'non_field_errors': ['User is not an admin']}}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({'errors': {'non_field_errors': ['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DashboardView(APIView):
    def get(self, request, format=None):
        return render(request, 'dashboard.html')

class tokenAuthenticateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        return Response(status=status.HTTP_200_OK)  

class ManageIPOView(APIView):
    def get(self, request, format=None):
        return render(request, 'manageipo.html')
